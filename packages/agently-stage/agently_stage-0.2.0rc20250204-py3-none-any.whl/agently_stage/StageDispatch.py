import time
import atexit
import inspect
import asyncio
import threading
import functools
from concurrent.futures import ThreadPoolExecutor
from .StageException import StageException

class StageDispatchEnvironment:
    def __init__(
            self,
            *,
            exception_handler,
            max_workers,
            is_daemon,
        ):
        self._exception_handler = exception_handler
        self._max_workers = max_workers
        self._is_daemon = is_daemon
        self._lock = threading.Lock()
        self.loop = None
        self.loop_thread = None
        self.executor = None
        self.exceptions = None
        self.ready = threading.Event()
        self._start_loop_thread()
        self.ready.wait()
        atexit.register(self.close)
    
    # Start Environment
    def _start_loop(self):
        self.loop = asyncio.new_event_loop()
        self.executor = ThreadPoolExecutor(max_workers=self._max_workers)
        self.loop.set_default_executor(self.executor)
        self.exceptions = StageException()
        self.loop.set_exception_handler(self._loop_exception_handler)
        asyncio.set_event_loop(self.loop)
        self.loop.call_soon_threadsafe(lambda: self.ready.set())
        self.loop.run_forever()

    def _start_loop_thread(self):
        with self._lock:
            if not self.ready.is_set():
                self.loop_thread = threading.Thread(
                    target=self._start_loop,
                    name="AgentlyStageDispatchThread",
                    daemon=self._is_daemon,
                )
                self.loop_thread.start()
                self.ready.wait()
    
    # Handle Exception
    def _loop_exception_handler(self, loop, context):
        if self._exception_handler is not None:
            if inspect.iscoroutinefunction(self._exception_handler):
               loop.call_soon_threadsafe(
                   lambda e: asyncio.ensure_future(self._exception_handler(e)),
                   context["exception"]
                )
            elif inspect.isfunction(self._exception_handler):
                loop.call_soon_threadsafe(self._exception_handler, context["exception"])
        else:
            self.exceptions.add_exception(context["exception"] if "exception" in context else RuntimeError(context["message"]), context)
            raise context["exception"]

    def raise_exception(self, e):
        def _raise_exception(e):
            raise e
        self.loop.call_soon(_raise_exception, e)
    
    def close(self):
        if self.ready.is_set():
            with self._lock:
                # Close all pending
                if self.loop:
                    pending = asyncio.all_tasks(self.loop)
                    if pending:
                        for task in pending:
                            task.cancel()
                        try:
                            asyncio.run_coroutine_threadsafe(
                                asyncio.gather(*pending, return_exceptions=True),
                                self.loop,
                            )
                        except:
                            pass
                # Stop loop
                if self.loop and self.loop.is_running():
                    self.loop.call_soon_threadsafe(self.loop.stop)
                # Join Thread
                if self.loop_thread and self.loop_thread.is_alive():
                    self.loop_thread.join()
                    self.loop_thread = None
                # Close loop
                if self.loop and not self.loop.is_closed():
                    self.loop.close()
                # Shutdown executor
                self.executor.shutdown(wait=True)
                # Clean
                self.loop_thread = None
                self.loop = None
                self.executor = None
                self.exceptions = None
                self.ready.clear()                

class StageDispatch:
    _instance = None
    _dispatch_env = None
    _lock = threading.Lock()

    def __new__(
        cls,
        *,
        exception_handler=None,
        max_workers=None,
        is_daemon=True,
    ):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._dispatch_env = StageDispatchEnvironment(
                        exception_handler=exception_handler,
                        max_workers=max_workers,
                        is_daemon=is_daemon,
                    )
                    def shutdown_at_exit():
                        cls._instance.ensure_tasks_done()
                        cls._dispatch_env.close()
                    atexit.register(shutdown_at_exit)
        return cls._instance

    def __init__(
            self,
            *,
            exception_handler=None,
            max_workers=None,
            is_daemon=True,
        ):
        self._all_tasks = set()
        self._dispatch_env = StageDispatch._dispatch_env
        self.raise_exception = self._dispatch_env.raise_exception
    
    def _register_task(self, task):
        with StageDispatch._lock:
            self._all_tasks.add(task)
        
        def _discard_form_tasks(_):
            with StageDispatch._lock:
                self._all_tasks.discard(task)
        task.add_done_callback(_discard_form_tasks)
    
    def run_sync_function(self, func, *args, **kwargs):
        task = self.to_executor(func, *args, **kwargs)
        self._register_task(task)
        return task
    
    def run_async_function(self, func, *args, **kwargs):
        if inspect.iscoroutinefunction(func):
            coro = func(*args, **kwargs)
        elif inspect.iscoroutine(func):
            coro = func
        task = asyncio.run_coroutine_threadsafe(
            coro,
            loop=self._dispatch_env.loop,
        )
        self._register_task(task)
        return task
    
    def to_executor(self, func, *args, **kwargs):
        return self._dispatch_env.executor.submit(func, *args, **kwargs)
    
    def ensure_tasks_start(self):
        def get_pending_tasks():
            with self._lock:
                pending_tasks = [task for task in self._all_tasks if not (task.running() or task.done())]    
            return pending_tasks
        
        while get_pending_tasks():
            time.sleep(0.01)
    
    def ensure_tasks_done(self):
        with self._lock:
            all_tasks = list(self._all_tasks)
        
        if len(all_tasks) > 0:
            for task in all_tasks:
                task.result()
            self.ensure_tasks_done()
    
    def close(self):
        self.ensure_tasks_done()
        if StageDispatch._instance is not None:
            with self._lock:
                if StageDispatch._instance is not None:
                    StageDispatch._dispatch_env.close()
                    StageDispatch._instance = None
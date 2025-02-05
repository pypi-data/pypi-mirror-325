# endcoding = utf-8
"""
author : vex1023
email :  vex1023@qq.com
各类型的decorator
"""

import signal
import time
import logging

from typing import (
    Callable,
    Tuple,
    Any,
    Type,
    Literal,
    Deque,
)
from multiprocessing import Lock
from functools import wraps

__all__ = [
    "retry",
    "timeit",
    "singleton",
    "timeout",
    "async_task",
    "async_map",
    "timer",
    "VXAsyncResult",
    "rate_limit",
]


###################################
# 错误重试方法实现
# @retry(tries, CatchExceptions=(Exception,), delay=0.01, backoff=2)
###################################


class retry:
    def __init__(
        self,
        tries: int,
        catch_exceptions: Tuple[Type[Exception]],
        delay: float = 0.1,
        backoff: int = 2,
    ) -> None:
        """重试装饰器

        Arguments:
            tries {int} -- 重试次数
            cache_exceptions {Union[Exception, Sequence[Exception]]} -- 发生错误时，需要重试的异常列表

        Keyword Arguments:
            delay {float} -- 延时时间 (default: {0.1})
            backoff {int} -- 延时时间等待倍数 (default: {2})
        """
        if backoff <= 1:
            raise ValueError("backoff must be greater than 1")

        if tries < 0:
            raise ValueError("tries must be 0 or greater")

        if delay <= 0:
            raise ValueError("delay must be greater than 0")

        self._catch_exceptions: Tuple[Type[Exception]] = (Exception,)
        if catch_exceptions:
            self._catch_exceptions = catch_exceptions

        self._tries = tries
        self._delay = delay
        self._backoff = backoff

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            mdelay = self._delay
            for i in range(1, self._tries):
                try:
                    return func(*args, **kwargs)
                except self._catch_exceptions as err:
                    logging.error(
                        "function %s(%s, %s) try %s times error: %s\n",
                        func.__name__,
                        args,
                        kwargs,
                        i,
                        err,
                    )
                    logging.warning("Retrying in %.4f seconds...", mdelay)

                    time.sleep(mdelay)
                    mdelay *= self._backoff

            return func(*args, **kwargs)

        return wrapper


###################################
# 计算运行消耗时间
# @timeit
###################################


class timer:
    """计时器"""

    def __init__(self, descriptions: str = "", *, warnning: float = 0) -> None:
        self._descriptions = descriptions
        self._start = 0.0
        self._warnning = warnning * 1000
        self._end = 0.0

    @property
    def cost(self) -> float:
        return (
            (time.perf_counter() if self._end == 0 else self._end) - self._start
        ) * 1000

    def __enter__(self) -> "timer":
        logging.debug(f"{self._descriptions} start...")
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self._end = time.perf_counter()

        if self.cost > self._warnning > 0:
            logging.warning(f"{self._descriptions} used : {self.cost:.2f}ms")
        else:
            logging.debug(f"{self._descriptions} used : {self.cost:.2f}ms")


class timeit:
    """
    计算运行消耗时间
    @timeit(0.5)
    def test():
        time.sleep(1)
    """

    def __init__(self, warnning_time: int = 5) -> None:
        self._warnning_time = warnning_time

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with timer(
                f"{func.__name__}({args},{kwargs})", warnning=self._warnning_time
            ):
                return func(*args, **kwargs)

        return wrapper


###################################
# Singleton 实现
# @singleton
###################################


class singleton(object):
    """
    单例
    example::

        @singleton
        class YourClass(object):
            def __init__(self, *args, **kwargs):
                pass
    """

    def __init__(self, cls: Type[Any]) -> None:
        self._instance = None
        self._cls = cls
        self._lock = Lock()

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self._instance is None:
            with self._lock:
                if self._instance is None:
                    self._instance = self._cls(*args, **kwargs)
        return self._instance


###################################
# 限制超时时间
# @timeout(seconds, error_message='Function call timed out')
###################################


# class TimeoutError(Exception):
#    pass


class timeout:
    def __init__(
        self, seconds: float = 1, *, timeout_msg: str = "Function %s call time out."
    ) -> None:
        self._timeout = seconds
        self._timeout_msg = timeout_msg

        pass

    def __call__(self, func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            signal.signal(signal.SIGALRM, self._handle_timeout)  # type: ignore[attr-defined]
            signal.alarm(self._timeout)  # type: ignore[attr-defined]
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)  # type: ignore[attr-defined]

        return wrapper

    def _handle_timeout(self, signum: int, frame: Any) -> None:
        raise TimeoutError(
            f"{self._timeout_msg} after {self._timeout * 1000}ms,{signum},{frame}"
        )


class RateOverLimitError(RuntimeError):
    pass


class rate_limit:
    def __init__(
        self,
        limits: int = 1,
        peroid: float = 1.0,
        if_over_limit: Literal["raise", "wait"] = "wait",
    ) -> None:
        self._peroid = peroid
        self._records: Deque[float] = Deque(maxlen=limits)
        self._records.append(0)
        self._if_over_limit = if_over_limit
        self._lock = Lock()

    def __call__(self, func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with self._lock:
                now = time.perf_counter()
                if self._records[0] > now - self._peroid:
                    if self._if_over_limit == "wait":
                        time.sleep(self._peroid - (now - self._records[0]))
                        now = time.perf_counter()
                    else:
                        raise RateOverLimitError(
                            f"Call limit {self._records.maxlen} times per {self._peroid} seconds"
                        )
                self._records.append(now)
            return func(*args, **kwargs)

        return wrapper


if __name__ == "__main__":
    from vxutils import loggerConfig
    from contextlib import suppress
    import logging

    loggerConfig()

    @rate_limit(3, 10)
    def test(i: int = 10) -> None:
        print("test")

    with timer("test timer", warnning=0.001) as t, suppress(RuntimeError):
        for i in range(10):
            test()
            time.sleep(0.5)

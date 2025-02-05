import asyncio
import functools
import hashlib
from typing import Callable, Any
from diskcache import Cache

class _ReturnValueException(Exception):

    def __init__(self, return_value: Any):
        super().__init__()
        self.return_value = return_value

class DoNotCache(_ReturnValueException):
    pass

class DeleteCache(_ReturnValueException):
    pass


def cached(cache_path: str|None=None, cache_key: str|Callable[[Any, list[Any], dict[str, Any]], str]|None=None, ttl: float|None=None):
    """
    A decorator to cache the results of async or regular functions using diskcache.
    """
    with Cache(cache_path) as cache:

        def decorator(func):
            is_async = asyncio.iscoroutinefunction(func)

            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                if callable(cache_key):
                    the_key = cache_key(func, args, kwargs)
                else:
                    the_key = cache_key or _generate_cache_key(func, *args, **kwargs)
                cached_result = cache.get(the_key)

                if cached_result is not None:
                    return cached_result

                try:
                    result = await func(*args, **kwargs)
                except DoNotCache as dnc:
                    return dnc.return_value
                except DeleteCache as dc:
                    cache.delete(the_key)
                    return dc.return_value
                else:
                    cache.set(the_key, result, expire=ttl)  # Set with optional TTL
                return result

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                if callable(cache_key):
                    the_key = cache_key(func, args, kwargs)
                else:
                    the_key = cache_key or _generate_cache_key(func, *args, **kwargs)
                cached_result = cache.get(the_key)

                if cached_result is not None:
                    return cached_result
                try:
                    result = func(*args, **kwargs)
                except DoNotCache as dnc:
                    return dnc.return_value
                except DeleteCache as dc:
                    cache.delete(the_key)
                    return dc.return_value
                else:
                    cache.set(the_key, result, expire=ttl)  # Set with optional TTL
                return result

            return async_wrapper if is_async else sync_wrapper

    return decorator


def _generate_cache_key(func, *args, **kwargs):
    """Generates a cache key based on the function name and arguments."""

    args_str = str(args)
    kwargs_str = str(kwargs)

    combined = f"{func.__name__}:{args_str}:{kwargs_str}"
    return hashlib.md5(combined.encode()).hexdigest()  # Use hash for key


# Example Usage:

@cached(ttl=10) 
async def my_async_function(a, b):
    await asyncio.sleep(2)  # Simulate some work
    return a + b

@cached(ttl=10) 
def my_sync_function(x, y):
  from time import sleep
  sleep(2)
  return x * y

async def demo():
    from time import time

    t0 = time()
    result1 = await my_async_function(2, 3)  # First call, will execute
    t1 = time()
    print(f"Non-cached call of my_async_function took {t1-t0:.2f} seconds")
    result2 = await my_async_function(2, 3)  # Second call, will retrieve from cache
    t2 = time()
    print(f"Cached call of my_async_function took {t2-t1:.2f} seconds")

    result3 = my_sync_function(4,5) # First call, will execute
    t3 = time()
    print(f"Non-cached call of my_sync_function took {t3-t2:.2f} seconds")

    result4 = my_sync_function(4,5) # Second call, will retrieve from cache
    t4 = time()
    print(f"Cached call of my_sync_function took {t4-t3:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(demo())
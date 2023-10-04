from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_archive = {}

    def inner(*args, **kwargs) -> Any:
        if args in cache_archive:
            print("Getting from cache")
        else:
            cache_archive[args] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_archive[args]
    return inner

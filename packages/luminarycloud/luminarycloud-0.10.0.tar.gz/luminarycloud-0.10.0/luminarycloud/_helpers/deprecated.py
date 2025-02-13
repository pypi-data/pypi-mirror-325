import warnings
from functools import wraps
from typing import Callable


def deprecated(reason: str) -> Callable[[Callable], Callable]:

    def decorator(f: Callable) -> Callable:

        @wraps(f)
        def new_func(*args, **kwargs):
            warnings.warn(
                f"{f.__name__} is deprecated: {reason}", category=DeprecationWarning, stacklevel=2
            )
            return f(*args, **kwargs)

        return new_func

    return decorator

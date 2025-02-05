import time
from functools import wraps
from typing import Any, Callable, Type, Tuple, Optional
import logging

logger = logging.getLogger(__name__)

def retry_with_backoff(
    retries: int = 3,
    backoff_in_seconds: int = 1,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Retry decorator with exponential backoff."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retry_count = 0
            while retry_count < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retry_count += 1
                    if retry_count == retries:
                        raise
                    
                    wait_time = (backoff_in_seconds * 2 ** retry_count)
                    logger.warning(
                        f"Attempt {retry_count} failed: {str(e)}. "
                        f"Retrying in {wait_time} seconds..."
                    )
                    time.sleep(wait_time)
            return None
        return wrapper
    return decorator

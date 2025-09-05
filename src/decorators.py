import functools
import sys
import traceback

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = (f"{func.__name__} error: {error_type}. "
                               f"Inputs: {args}, {kwargs}\n")
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")
                raise  # не проглатываем ошибку
        return wrapper
    return decorator
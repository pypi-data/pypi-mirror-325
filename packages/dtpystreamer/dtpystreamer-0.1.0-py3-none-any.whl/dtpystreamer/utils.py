import time


def retry_on_failure(func):
    def wrapper(*args, **kwargs):
        retries = 5
        delay = 1
        for attempt in range(1, retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == retries:
                    raise e
                time.sleep(delay)
                delay *= 2

    return wrapper

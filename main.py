
from functools import lru_cache, wraps
import time


def log(log_file='log.txt'):
    def decor(func):
        @wraps(func)
        def fibonacci_log(n):
            result = func(n)
            with open(log_file, 'a') as f:
                f.write(f'n = {n} f = {result}\n')
            return result
        return fibonacci_log
    return decor


@lru_cache(maxsize=32)
@log()
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci.__name__)
start = time.time()
print(list(fibonacci(n) for n in range(20)))
end = time.time()
print(end - start)

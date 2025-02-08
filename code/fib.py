import time
import functools

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_elapsed = end - start
        
        print(f"Finished in {time_elapsed:.6f}s: f({args[0]}) -> {result}")
        return result
    return wrapper

execution_times = {}

@functools.lru_cache
@timer
def fib(n):
    start = time.time()

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)

    end = time.time()
    execution_times[n] = end - start
    return result

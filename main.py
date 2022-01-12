import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, *kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer

@timer
def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("enter a number of sequence members "))
print("fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))     # убрал отсюда end='' так как и без того результат "полная дичь, но работает!"
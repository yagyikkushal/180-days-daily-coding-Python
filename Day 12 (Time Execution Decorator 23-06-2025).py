# Creating a Python decorator to measure function execution time
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time Taken:", end - start)
        return result

    return wrapper


@timer
def loop(x):
    for _ in range(x):
        a = 5
    return a


result = loop(100000)
print(result)

# Create a Decorator to Log Function Arguments and Return Value

def decofunc(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} result: {result}")

        return result

    return wrapper


@decofunc
def multiply_numbers(x, y):
    return x * y


result = multiply_numbers(2, 3)

print("Result:", result)
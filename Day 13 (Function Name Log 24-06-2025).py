# Write a Python decorator that logs the function name, its input parameters, and output to the console using print().

def decolog(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is called with input parameters {args} {kwargs}")
        func(*args, **kwargs)

    return wrapper

@decolog
def printing(age):
    print(f"Kushal Yagyik is {age}")

printing(25)

@decolog
def calling(name):
    print(f"I am calling {name}")

calling(name="Kushal")
# Write a Python decorator that conditionally logs calls based on a debug flag passed as an argument to the decorator.


def conditionally_log_calls(argument="nodebug"):
    def decorator(func):
        def wrapper():
            if argument == "debug":
                print(f'{func.__name__} is called conditionally.')
                return func()
            else:
                return func()

        return wrapper

    return decorator


@conditionally_log_calls()
def say_name():
    print("Kushal")


@conditionally_log_calls("debug")
def say_age():
    print("25")


@conditionally_log_calls("debug")
def say_city():
    print("Kanpur")


say_name()
say_age()
say_city()
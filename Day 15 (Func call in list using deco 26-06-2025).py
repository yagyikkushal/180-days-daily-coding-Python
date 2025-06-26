# Write a Python decorator that stores the log of a function call in a global list for later analysis.

mylist = []


def deco_log_list(func):
    def wrapper(*args, **kwargs):
        mylist.append(func.__name__)
        result = func(*args, **kwargs)
        return result

    return wrapper


@deco_log_list
def kushal(n):
    a = n
    print("testing")
    return a


@deco_log_list
def uddyan(n):
    a = n
    print("testing 2")
    return a


kushal(6)
uddyan(5)

print(mylist)
# Write a Python decorator that writes the function’s arguments and return value to a file each time the function is called.

def deco(func):
    def wrapper(*args):
        print(f"args: {','.join(str(arg) for arg in args)}")
        res = func(*args)
        with open("file.txt", "w") as f:
            f.write(str(res))
        return res

    return wrapper


@deco
def name(x):
    a = x
    print("Kushal")
    return a


name(5)
name(6)

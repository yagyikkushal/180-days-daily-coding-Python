def fib_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

fib = fib_gen()

for _ in range(10):
    print (next(fib))
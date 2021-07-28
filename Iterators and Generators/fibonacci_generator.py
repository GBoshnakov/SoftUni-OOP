def fibonacci():
    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n-2) + fib(n-1)

    i = 0
    while True:
        yield fib(i)
        i += 1


generator = fibonacci()
for i in range(10):
    print(next(generator))

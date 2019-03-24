def fibo(n):
    fib = [None] * (n)
    if n == 0 or n == 1:
        return 1
    fib[0] = 1
    fib[1] = 1

    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i -2]
    return fib[n-1]

print(fibo(9))
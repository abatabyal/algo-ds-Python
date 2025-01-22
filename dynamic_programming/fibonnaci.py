def fibo(n):
    memo = {}
    if n in memo:
        return memo[n]
    else:
        if n <= 2:
            memo[n] = 1
        else:
            memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(9))
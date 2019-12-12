#bottom up approach
def fact_bua(n):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = dp[i-1] * i
    return dp

fact_bua(5)

# memoization
def fact_memo(n):
    dp = [0] * n

    if n == 0:
        return 1
    if dp[n]:
        return dp[n]
    dp[n] = n * solve(n - 1)
    return dp[n]

fact_memo(5)
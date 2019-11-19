def knapsack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    wt = [v * 2 for v in val]
    # k[][] bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max((val[i-1] + K[i-1][w-wt[i-1]]), (K[i-1][w]))
            else:
                K[i][w] = K[i-1][w]

    res = K[n][W]
    print(res)

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            # This item is included.
            print(wt[i - 1])
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

val = [3, 2, 2]
wt = [3, 2, 2]
W = 9
n = len(val)
knapsack(W, wt, val, n)
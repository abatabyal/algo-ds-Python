class Interval:
    buy = 0
    sell = 0

def stock_trade(arr, n):
    if n == 1:
        return

    count = 0
    sol = []
    i = 0
    while i < n-1:
        while i < n-1 and arr[i+1] <= arr[i]:
            i += 1
        if i == n-1:
            break

        #store index of minima
        e = Interval()
        e.buy = i+1

        while i < n and arr[i] >= arr[i-1]:
            i += 1

        # maxima
        e.sell = i - 1
        sol.append(e)
        count += 1
        i += 1

    if count == 0:
        print("No Profit")
    else:
        for i in range(count):
            print("Buy on day: " + sol[i].buy + " Sell on dat: " + sol[i].sell)

price = [100, 180, 260, 310, 40, 535, 695 ]
n = len(price)
stock_trade(price, n)
import math
# Recursion exponential time
def fibo_recursion(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_formulae(n):
    # Fn = {[(√5 + 1)/2] ^ n} / √5
    x = pow(((math.sqrt(5) + 1) / 2 ), n) / math.sqrt(5)
    return round(x)
print(fibo_formulae(9))
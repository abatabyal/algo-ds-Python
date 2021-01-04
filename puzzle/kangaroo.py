def kangaroo(x1, v1, x2, v2):
    if abs(x1-x2) % gcd(v1,v2) == 0:
        return "YES"
    else:
        return "NO"

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(kangaroo(0, 2, 5, 3))
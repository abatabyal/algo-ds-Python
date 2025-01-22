def check_pow_2(n):
    return True if n & n-1 == 0 else False

print(check_pow_2(4))
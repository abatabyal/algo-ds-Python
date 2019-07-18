def clear_bit(n, k):
    return (n & ~(1 << (k -1)))

def toggle_bit(n, k):
    return n ^ (1 << k-1)

def toggle_rmb(n):
    return n & n-1

def self_and(n):
    return n & n

val = self_and(0b01001011)
print(val)
print(int('01001011', 2))
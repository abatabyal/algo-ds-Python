def clear_bit(n, k):
    return (n & ~(1 << (k -1)))

def toggle_bit(n, k):
    return n ^ (1 << k-1)

def toggle_rmb(n):
    return n & n-1

def self_and(n):
    return n & n

def odd_even(n):
     if (n & 1):
         return 'odd'
     else:
         return 'even'

print(odd_even(5))
# A Python3 code program
# to check for even or odd

# Returns true if n is even, else odd
def isEven(n):
    # n&1 is 1, then odd, else even
    x = n & 1
    return (not(n & 1))


# Driver code
n = 10;
print("Even" if isEven(n) else "Odd")

arr = ["Even", "Odd"]
print ("Enter the number")
no = input()
print (arr[int(no) % 2])
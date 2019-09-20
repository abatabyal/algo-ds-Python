def swap(x, y):
    # Check if the two addresses are same
    if (id(x) == id(y)):
        return
    x = x ^ y
    y = x ^ y
    x = x ^ y

# Driver code
x = 10
y = 20
swap(x, y)
print("After swap(&x, &x): x = ", x)
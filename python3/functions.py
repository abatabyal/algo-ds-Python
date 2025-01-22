from collections import Counter

# Nested Function
def outer_function(text):
    text = text

    def inner_function():
        print(text)

    inner_function()

# Closure
def o_func(text):
    text = text

    def i_func(text):
        print(text)
    return i_func

# Map Function
def double_money(inr):
    return  inr * 2

# most_common function
arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]
counter = Counter(arr)
top_three = counter.most_common(1)
print(top_three)
outer_function('Hello')
o_func('Closure')
income = [10, 30, 75]
print(list(map(double_money, income)))
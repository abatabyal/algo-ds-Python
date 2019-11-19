def countApplesAndOranges(s, t, a, b, apples, oranges):
    post_apple_values = [a + i for i in apples]
    post_orange_values = [b + i for i in oranges]
    print(post_orange_values)
    apple_count = 0
    orange_count = 0
    for a in post_apple_values:
        if a >= s and a <= t:
            apple_count += 1

    for o in post_orange_values:
        if o >= s and o <= t:
            orange_count += 1

    return  apple_count, orange_count

s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apple = [-2, 2, 1]
oranges = [5, -6]
print(countApplesAndOranges(s, t, a, b, apple, oranges))
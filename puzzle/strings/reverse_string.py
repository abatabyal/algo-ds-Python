def reverse_string(a):
    words = a.split('.')
    for i in range(len(words), 0, -1):
        if i == 1:
            print(words[i-1])
        else:
            print(words[i-1], end='.')

test_cases = int(input())
for i in range(test_cases):
    a = str(input())
    reverse_string(a)
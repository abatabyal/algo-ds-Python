def remove_duplicates(a):
    frequency = {}
    order = []
    for c in a:
        if c in frequency:
            frequency[c] = frequency[c] + 1
        else:
            frequency[c] = 1
            order.append(c)
    for k in order:
        print(k,end='')
    print('\r')

test_cases = int(input())
for i in range(test_cases):
    a = str(input())
    remove_duplicates(a)
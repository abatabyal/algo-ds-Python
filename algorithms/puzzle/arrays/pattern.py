arr = [-1, 2, 3]
max_arr = max(arr)
print(max_arr)
for e in arr:
    if e < 0:
        for i in range(max_arr):
            print('\n')
        for i in range(abs(e)):
            print('*')
    else:
        for i in range(max_arr - e):
            print('\n')
        for i in range(e):
            print('*')
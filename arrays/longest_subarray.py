def min(x, y):
    return x if (x < y) else y

def max(x, y):
    return x if (x > y) else y

def find_length(arr):

    max_len = 1
    n = len(arr)

    for i in range(n - 1):
        _min = arr[i]
        _max = arr[i]

        for j in range(i + 1, n):

            _min = min(_min, arr[j])
            _max = max(_max, arr[j])

            if ((_max - _min ) == j - i):
                max_len = max(max_len, _max - _min + 1)

    return max_len

arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
find_length(arr)
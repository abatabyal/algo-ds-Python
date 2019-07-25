def missing_number(n, arr):
    sum_of_n = int(n * (n + 1) / 2)

    sum_current = 0
    for i in range(len(arr)):
        sum_current += arr[i]

    miss_num = sum_of_n - sum_current

    return miss_num

test_cases = int(input())
for i in range(test_cases):
    size_of_array = int(input())
    arr = list(map(int, input().split()))
    num = missing_number(size_of_array, arr)
    print(int(num))
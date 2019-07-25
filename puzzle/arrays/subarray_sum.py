def subarray_sum(n, sum_val, arr):
    curr_sum = 0
    for i in range(n):
        for





test_cases = int(input())
for i in range(test_cases):
    size_of_array, sum_search_val = size_of_array, sum_search_val = list(map(str,input().split()))
    arr = list(map(int, input().split()))
    num = subarray_sum(size_of_array, sum_search_val, arr)
    print(int(num))
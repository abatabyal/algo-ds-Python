def equilibrium_point(n, arr):
    sum_array = 0
    for i in arr:
        sum_array += i

    left_sum = right_sum = 0
    eq = 0
    for i in range(len(arr) - 1):
        left_sum += arr[i]
        right_sum = sum_array - (left_sum + arr[i+1])
        if left_sum == right_sum:
            print(i+2)
            eq = i + 2
    if eq != 0:
        return eq
    else:
        return -1


test_cases = int(input())
for i in range(test_cases):
    size_of_array = int(input())
    arr = list(map(int, input().split()))
    num = equilibrium_point(size_of_array, arr)
    print(int(num))


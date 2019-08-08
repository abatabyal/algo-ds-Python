def max_2(arr):
    max = 0
    max2 = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max2 = max
            max = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    return max, max2

arr = [3,4,66,5,11]
print(max_2(arr))
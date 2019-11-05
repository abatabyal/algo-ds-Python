def max_2_num(arr):
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
print(max_2_num(arr))

def max_3_num(arr):
    if len(arr) < 3:
        return
    max = 0
    max_2 = 0
    max_3 = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max_2 = max
            max_3 = max_2
            max = arr[i]
        elif arr[i] > max_2:
            max_3 = max_2
            max_2 = arr[i]
        elif arr[i] > max_3:
            max_3 = arr[i]
    return max_3

a = [5, 7, 99, -9, 89]
print(max_3_num(a))
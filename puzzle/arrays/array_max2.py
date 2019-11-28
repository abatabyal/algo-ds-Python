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
    first = 0
    second = 0
    third = 0
    for i in range(len(arr)):
        if arr[i] > first:
           third = second
           second = first
           first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]
    return third

a = [5, 7, 99, -9, 89]
print(max_3_num(a))

def max_4_num(arr):
    if len(arr) < 4:
        return
    first = 0
    second = 0
    third = 0
    fourth = 0
    for i in range(len(arr)):
        if arr[i] > first:
            fourth = third
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second:
            fourth = third
            third = second
            second = arr[i]
        elif arr[i] > third:
            fourth = third
            third = arr[i]
        elif arr[i] > fourth:
            fourth = arr[i]
    return fourth + third + second + first

a = [1, 2, 3, 4, 12, 34]
print(max_4_num(a))
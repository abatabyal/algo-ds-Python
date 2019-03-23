def binary_search(arr, l, r, x):

    if r >= 1:
        mid = l + (r - 1)/2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binary_search(arr, mid+1, r, x)
        else:
            return binary_search(arr, l, mid-1, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 2
result = binary_search(arr, 0, len(arr) - 1, x)
print(result)
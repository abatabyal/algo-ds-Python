def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i -1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def binary_search(arr, value, start, end):
    if start == end:
        if arr[start] > value:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) / 2
    if arr[mid] < value:
        return binary_search(arr, value, mid+1, end)
    elif arr[mid] > value:
        return binary_search(arr, value, start, mid-1)
    else:
        return mid

def binary_insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i-1)
        arr = arr[:j] + key + arr[j:i] + arr[i+1:]
    return arr
arr = [5,2,4, 6, 1, 3]
# insertion_sort(arr)
binary_insert_sort(arr)
for i in range(len(arr)):
    print (arr[i], end=',')


def majority_element(size_of_array, arr):
    maj_elem_size = size_of_array // 2
    frequency = {x: 0 for x in arr}
    for i in range(len(arr)):
        frequency[arr[i]] += 1
    maj_elem = -1
    for k,v in frequency.items():
        if v > maj_elem_size:
            maj_elem = k
    return maj_elem

test_cases = int(input())
for i in range(test_cases):
    size_of_array = int(input())
    arr = list(map(int, input().split()))
    num = majority_element(size_of_array, arr)
    print(int(num))
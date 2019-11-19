def cut_the_sticks(arr):
    op_list = []
    op_list.append(len(arr))
    arr.sort()
    while(sum(arr) != 0):
        min_arr = min(i for i in arr if i != 0)
        for i in range(len(arr)):
            if arr[i] > 0:
                arr[i] = arr[i] - min_arr
        len_count = 0
        for a in arr:
            if a != 0:
                len_count += 1
        if len_count == 0:
            break
        op_list.append(len_count)
        if len_count == 1:
            break
    return op_list

arr = [8,8,14,10,3,5,14,12]
print(cut_the_sticks(arr))




def split(arr_list: list) -> list:
    """

    :param arr_list: input list
    :return: splits the input list in two halves
    Used for loop instead of split function to reduce time complexity.O(logn)
    split function increases time complexity to O(kn)
    """
    left_half = []
    right_half = []
    size = len(arr_list)
    midpoint = size // 2
    for i in range(midpoint):
        left_half.append(arr_list[i])
    for midpoint in range(midpoint, size):
        right_half.append(arr_list[midpoint])
    return left_half, right_half


def merge(left: list, right: list) -> list:
    """

    :param left:
    :param right:
    :return:
    takes O(n)
    """
    sorted_merged = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_merged.append(left[l])
            l += 1
        else:
            sorted_merged.append(right[r])
            r += 1
    while l < len(left):
        sorted_merged.append(left[l])
        l += 1
    while r < len(right):
        sorted_merged.append(right[r])
        r += 1
    return sorted_merged


def merge_sort(arr_list: list) -> list:
    """

    :param arr_list:
    :return:
    O(nlogn)
    """
    if len(arr_list) <= 1:
        return arr_list
    left_half, right_half = split(arr_list)

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)


input_list = [55, 27, 32]
print(merge_sort(input_list))

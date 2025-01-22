def get_single_element(arr):
    ones = 0
    twos = 0

    n = len(arr)
    for i in range(n):
        twos = twos | (ones & arr[i])

        ones = ones ^ arr[i]

        common_bit_mask = ~(ones & twos)

        ones &= common_bit_mask

        twos &= common_bit_mask
    return ones

arr = [3,3,3,2]
print(get_single_element(arr))
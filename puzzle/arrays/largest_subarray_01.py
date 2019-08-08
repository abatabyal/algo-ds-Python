def largest_subarray(n, arr):
    zeros = 0
    ones = 0
    for a in arr:
        if a == 0:
            zeros += 1
        else:
            ones += 1
    print(zeros)
    print(ones)

    if zeros <= ones:
        if zeros == 1:
            print(zeros + 1)
            return zeros + 1
        else:
            print(2 * zeros)
            return 2 * zeros
    else:
        if ones == 1:
            print(ones + 1)
            return ones + 1
        else:
            print(2 * ones)
            return 2 * ones

test_cases = int(input())
for i in range(test_cases):
    size_of_array = int(input())
    arr = list(map(int, input().split()))
    num = largest_subarray(size_of_array, arr)
    print(int(num))
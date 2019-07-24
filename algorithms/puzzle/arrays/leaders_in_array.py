def leaders_in_array(n, arr):



test_cases = int(input())
for i in range(test_cases):
    size_of_array = int(input())
    arr = list(map(int, input().split()))
    num = leaders_in_array(size_of_array, arr)
    print(int(num))
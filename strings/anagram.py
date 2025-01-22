def anagram(a,b):
    if sorted(a) == sorted(b):
        print("YES")
    else:
        print('NO')

test_cases = int(input())
for i in range(test_cases):
    a, b = a, b = list(map(str, input().split()))
    anagram(a, b)
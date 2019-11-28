import sys
def hourglassSum(arr):
    max_hourglass_sum = -sys.maxsize -1
    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if sum > max_hourglass_sum:
                max_hourglass_sum = sum
    return max_hourglass_sum

arr = [[-1,-1,0,-9,-2,-2],
       [-2,-1,-6,-8,-2,-5],
       [-1,-1,-1,-2,-3,-4],
       [-1,-9,-2,-4,-4,-5],
       [-7,-3,-3,-2,-9,-9],
       [-1,-3,-1,-2,-4,-5]]
print(hourglassSum(arr))

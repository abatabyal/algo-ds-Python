def preProcess(mat):
    M = len(mat)
    N = len(mat[0])
    aux = [[0 for i in range(N)]
           for j in range(M)]
    # Copy first row of mat[][] to aux[][]
    for i in range(0, N, 1):
        aux[0][i] = mat[0][i]

        # Do column wise sum
    for i in range(1, M, 1):
        for j in range(0, N, 1):
            aux[i][j] = mat[i][j] + aux[i - 1][j]

            # Do row wise sum
    for i in range(0, M, 1):
        for j in range(1, N, 1):
            aux[i][j] += aux[i][j - 1]

        # A O(1) time function to compute sum of submatrix
    return aux
# between (tli, tlj) and (rbi, rbj) using aux[][]
# which is built by the preprocess function
def sumQuery(aux, c1, c2):

    tli = int(c1.split(',')[0])
    tlj = int(c1.split(',')[1])
    rbi = int(c2.split(',')[0])
    rbj = int(c2.split(',')[1])
    # result is now sum of elements
    # between (0, 0) and (rbi, rbj)
    res = aux[rbi][rbj]

    # Remove elements between (0, 0)
    # and (tli-1, rbj)
    if (tli > 0):
        res = res - aux[tli - 1][rbj]

        # Remove elements between (0, 0)
    # and (rbi, tlj-1)
    if (tlj > 0):
        res = res - aux[rbi][tlj - 1]

        # Add aux[tli-1][tlj-1] as elements
    # between (0, 0) and (tli-1, tlj-1)
    # are subtracted twice
    if (tli > 0 and tlj > 0):
        res = res + aux[tli - 1][tlj - 1]

    return res
arr = [[1,2,3,4], [5,6,7,8], [8,7,6,5], [4,3,2,1]]
aux  = preProcess(arr)
c1 = '0, 0'
c2 = '0, 3'
print(sumQuery(aux, c1,c2))


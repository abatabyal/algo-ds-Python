N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end='')
        print('\r')

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col):
    # base case
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_nq_util(board, col+1) == True:
                return True

            board[i][col] = 0
    return False

def solve_nq():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]
    if solve_nq_util(board, 0) == False:
        print("No Solution")
        return False

    printSolution(board)

solve_nq()
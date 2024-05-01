def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(" Q " if board[i][j] == 1 else " . ", end="")
        print()
def solveNQUtil(board, col, ld, rd, cl):
    if col >= N:
        return True
    for i in range(N):
        if (ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
            if solveNQUtil(board, col + 1, ld, rd, cl):
                return True
            board[i][col] = 0
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
    return False
def solveNQ():
    global N
    N = int(input("Enter the value of N for N-Queens problem: "))
    board = [[0 for _ in range(N)] for _ in range(N)]
    ld = [0] * (2 * N - 1)
    rd = [0] * (2 * N - 1)
    cl = [0] * N
    if not solveNQUtil(board, 0, ld, rd, cl):
        print("Solution does not exist")
        return False
    printSolution(board)
    return True
if __name__ == "__main__":
    solveNQ()
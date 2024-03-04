def is_safe(board, row, col):
    return not any(board[i][col] or board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))) and \
           not any(board[i][col] or board[i][j] for i, j in zip(range(row, 8), range(col, -1, -1))) and \
           not any(board[row][i] for i in range(col))

def solve_queens(board, col):
    if col >= 8:
        return True
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 'Q' # Changed Q to 'Q' for string representation
            if solve_queens(board, col + 1):
                return board  # Return the board if a solution is found
            board[i][col] = '_' # Changed _ to '_' for string representation
    return False

def place_queens():
    board = [['_' for _ in range(8)] for _ in range(8)] # Changed 0 to '_' for string representation
    solution = solve_queens(board, 0)
    if solution:
        print("Solution:")
        [print(*row) for row in solution]
    else:
        print("No solution exists")

if __name__ == "__main__":
    place_queens()

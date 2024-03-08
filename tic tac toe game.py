def print_board(board):
    for row in board:
        print("|".join(row))
    print("\n")

board = [['-' for _ in range(3)] for _ in range(3)]
players = ['X', 'O']
current_player = 0

print_board(board)

while '-' in [cell for row in board for cell in row]:
    row, col = map(int, input(f"Player {players[current_player]}, enter row and column (0-2): ").split())
    if board[row][col] == '-':
        board[row][col] = players[current_player]
        print_board(board)
        for player in players:
            if [player] * 3 in board or [player] * 3 in zip(*board) or (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
                print(f"Player {player} wins!")
                break
        else:
            current_player = 1 - current_player
    else:
        print("Invalid move. Try again.")
else:
    print("It's a tie!")

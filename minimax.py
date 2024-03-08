import random

# Function to check if the game is over (determine the winner based on scores)
def game_over(scores):
    if scores['player1'] >= 100:
        return 'player1'
    elif scores['player2'] >= 100:
        return 'player2'
    else:
        return None

# Function to evaluate the game state using the Minimax algorithm
def minimax(scores, depth, is_maximizing):
    result = game_over(scores)
    if result is not None:
        if result == 'player1':
            return -1, None
        elif result == 'player2':
            return 1, None
        else:
            return 0, None

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for move in range(1, 11):
            scores['player2'] += move
            score, _ = minimax(scores, depth + 1, False)
            scores['player2'] -= move
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for move in range(1, 11):
            scores['player1'] += move
            score, _ = minimax(scores, depth + 1, True)
            scores['player1'] -= move
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

# Main function to play the game
def play_game():
    scores = {'player1': 0, 'player2': 0}
    current_player = 'player1'

    while game_over(scores) is None:
        if current_player == 'player1':
            print("Player 1's turn.")
            move = int(input("Enter player 1's move (1-10): "))
            scores['player1'] += move
            current_player = 'player2'
        else:
            print("Player 2's turn.")
            move = random.randint(1, 10)  # Generate a random move for Player 2
            print("Player 2 chooses move:", move)
            scores['player2'] += move
            current_player = 'player1'

    winner = game_over(scores)
    if winner == 'player1':
        print("Player 1 wins!")
    elif winner == 'player2':
        print("Player 2 wins!")
    else:
        print("It's a draw!")

# Start the game
play_game()

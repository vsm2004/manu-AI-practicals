import random
def hill_climbing(initial_state, goal_state, evaluate):
    current_state = initial_state
    while current_state != goal_state:
        neighbors = [(current_state[0] + random.choice([-1, 1]), current_state[1]), (current_state[0], current_state[1] + random.choice([-1, 1]))]
        next_state = max(neighbors, key=evaluate)
        if evaluate(next_state) <= evaluate(current_state):
            break
        current_state = next_state
    return current_state
initial_state = (0, 0)
goal_state = (5, 5)
evaluate = lambda state: -(abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1]))  # Example evaluation function
print(hill_climbing(initial_state, goal_state, evaluate))

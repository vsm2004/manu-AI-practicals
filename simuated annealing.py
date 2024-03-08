import numpy as np
import math
import random

def simulated_annealing(cost_function, initial_solution, temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    best_solution = current_solution
    current_cost = cost_function(current_solution)
    best_cost = current_cost

    for i in range(num_iterations):
        # Generate a random neighboring solution
        new_solution = generate_neighbor(current_solution)
        new_cost = cost_function(new_solution)

        # If the new solution is better, accept it
        if new_cost < current_cost:
            current_solution = new_solution
            current_cost = new_cost
            # Update the best solution if needed
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
        else:
            # If the new solution is worse, accept it with a probability based on the temperature
            if acceptance_probability(current_cost, new_cost, temperature) > random.random():
                current_solution = new_solution
                current_cost = new_cost

        # Cool the temperature
        temperature *= cooling_rate

    return best_solution, best_cost

def generate_neighbor(solution):
    # Example: Flip one randomly chosen bit in the solution
    neighbor = solution.copy()
    index = random.randint(0, len(solution) - 1)
    neighbor[index] = 1 - neighbor[index]  # Flip 0 to 1 or 1 to 0
    return neighbor

def acceptance_probability(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return 1.0
    else:
        return math.exp((current_cost - new_cost) / temperature)

# Example cost function: sum of squares
def cost_function(solution):
    return sum(x**2 for x in solution)

# Example usage
if __name__ == "__main__":
    # Define the problem parameters
    initial_solution = np.array([0, 0, 0, 0, 0])  # Initial solution
    temperature = 100.0  # Initial temperature
    cooling_rate = 0.95  # Cooling rate
    num_iterations = 1000  # Number of iterations

    # Run simulated annealing
    best_solution, best_cost = simulated_annealing(cost_function, initial_solution, temperature, cooling_rate, num_iterations)

    print("Best solution found:", best_solution)
    print("Best cost found:", best_cost)

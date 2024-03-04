from itertools import combinations

def is_valid(state):
    missionaries, cannibals = state
    return missionaries == 0 or missionaries >= cannibals

def solve():
    for left in combinations(range(4), 2):
        for right in combinations(range(4), 2):
            if is_valid((left.count(0) + right.count(0), left.count(1) + right.count(1))):
                return left, right

if __name__ == "__main__":
    left, right = solve()
    print("Solution:")
    print("Initial state: 3 missionaries, 3 cannibals, boat at left bank")
    print("Final state: 0 missionaries, 0 cannibals, boat at right bank")
    print("Moves:")
    for i, m in enumerate(left):
        c = left.count(1) - m
        print(f"Step {i+1}: {m} missionaries, {c} cannibals move from left to right")
    for i, m in enumerate(right):
        c = right.count(1) - m
        print(f"Step {i+len(left)+1}: {m} missionaries, {c} cannibals move from right to left")

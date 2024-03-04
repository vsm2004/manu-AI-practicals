import random
class SlidingPuzzle:
    def __init__(self):
        self.state = list(range(1, 9)) + [0] 
        random.shuffle(self.state) 
    def __str__(self):
        return '\n'.join([' '.join(map(str, self.state[i:i+3])) for i in range(0, 9, 3)])
    def move(self, number):
        empty_index = self.state.index(0)
        number_index = self.state.index(number)
        if (empty_index - number_index) in [-1, 1, -3, 3]:  
            self.state[empty_index], self.state[number_index] = self.state[number_index], self.state[empty_index]
        else:
            print("Invalid move")
    def is_solved(self):
        return self.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]
if __name__ == "__main__":
    puzzle = SlidingPuzzle()
    print("Initial State:")
    print(puzzle)
    while not puzzle.is_solved():
        move = int(input("Enter number to move (0 to quit): "))
        if move == 0:
            break
        puzzle.move(move)
        print(puzzle)
    if puzzle.is_solved():
        print("Congratulations! Puzzle solved.")
    else:
        print("Quitting...")

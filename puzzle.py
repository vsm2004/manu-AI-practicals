class SlidingPuzzle:
    def __init__(self):
        self.grid = [[1, 2, 3], [4, 5, 6], [7, 8, None]]  # None represents the empty space
        self.empty_pos = (2, 2)  # Initially the empty space is at (2, 2)
    
    def display(self):
        for row in self.grid:
            print(row)
    
    def move(self, direction):
        dx, dy = 0, 0
        if direction == "up":
            dx = -1
        elif direction == "down":
            dx = 1
        elif direction == "left":
            dy = -1
        elif direction == "right":
            dy = 1
        
        x, y = self.empty_pos
        new_x, new_y = x + dx, y + dy
        
        # Check if the move is valid
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Swap the empty space with the adjacent tile
            self.grid[x][y], self.grid[new_x][new_y] = self.grid[new_x][new_y], self.grid[x][y]
            self.empty_pos = (new_x, new_y)
        else:
            print("Invalid move!")
    
    def is_solved(self):
        return self.grid == [[1, 2, 3], [4, 5, 6], [7, 8, None]]


# Example usage:
puzzle = SlidingPuzzle()
puzzle.display()

while not puzzle.is_solved():
    direction = input("Enter direction (up/down/left/right): ").lower()
    puzzle.move(direction)
    puzzle.display()

print("Congratulations! You solved the puzzle!")

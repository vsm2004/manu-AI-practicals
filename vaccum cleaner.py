class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)
        self.direction = 'right'
        self.moves = 0

    def clean(self):
        dirty_cells = self.get_dirty_cells()
        while dirty_cells:
            if self.grid[self.position[0]][self.position[1]] == 'D':
                self.grid[self.position[0]][self.position[1]] = 'C'
                dirty_cells.remove(self.position)
            next_position = self.get_next_position()
            if next_position:
                self.position = next_position
                self.moves += 1
            else:
                break
            dirty_cells = self.get_dirty_cells()

    def get_dirty_cells(self):
        dirty_cells = set()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'D':
                    dirty_cells.add((i, j))
        return dirty_cells

    def get_next_position(self):
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        next_row = self.position[0] + directions[self.direction][0]
        next_col = self.position[1] + directions[self.direction][1]
        if 0 <= next_row < len(self.grid) and 0 <= next_col < len(self.grid[0]):
            return next_row, next_col
        else:
            self.change_direction()
            return None

    def change_direction(self):
        directions = ['up', 'right', 'down', 'left']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]


# Example usage:
grid = [['D', 'C', 'D', 'D'],
        ['D', 'D', 'C', 'C'],
        ['C', 'D', 'D', 'C'],
        ['D', 'C', 'D', 'D']]

vacuum_cleaner = VacuumCleaner(grid)
vacuum_cleaner.clean()
print("Grid after cleaning:")
for row in grid:
    print(row)
print("Total moves:", vacuum_cleaner.moves)


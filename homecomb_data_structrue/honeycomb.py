class Honeycomb:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = {(row, col): None for row in range(rows) for col in range(columns)}

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.grid[(row, col)] = value
        else:
            raise IndexError("Row and column indices are out of bounds")

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            return self.grid[(row, col)]
        else:
            raise IndexError("Row and column indices are out of bounds")

    def neighbors(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.columns):
            raise IndexError("Row and column indices are out of bounds")

        deltas = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1),   # right
            (-1, 1),  # up-right
            (1, -1)   # down-left
        ]

        neighbor_positions = [(row + dr, col + dc) for dr, dc in deltas]
        valid_neighbors = [(r, c) for r, c in neighbor_positions if 0 <= r < self.rows and 0 <= c < self.columns]
        return [self.grid[pos] for pos in valid_neighbors]

    def __repr__(self):
        representation = ""
        for row in range(self.rows):
            representation += " " * row  # Indentation for the honeycomb pattern
            for col in range(self.columns):
                representation += str(self.grid[(row, col)]) or "."
                representation += " " * 2
            representation += "\n"
        return representation

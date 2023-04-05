from honeycomb import Honeycomb
from three_sided_deque import ThreeSidedDeque

class HoneycombDataStructure:
    def __init__(self, rows, columns):
        self.honeycomb = Honeycomb(rows, columns)
        self.deques = {(row, col): ThreeSidedDeque() for row in range(rows) for col in range(columns)}

    def set(self, row, col, deque):
        if not isinstance(deque, ThreeSidedDeque):
            raise ValueError("Expecting a ThreeSidedDeque object")
        self.honeycomb.set(row, col, deque)

    def get(self, row, col):
        return self.honeycomb.get(row, col)

    def neighbors(self, row, col):
        return [self.deques[pos] for pos in self.honeycomb.neighbors(row, col)]

    def __repr__(self):
        return str(self.honeycomb)
This HoneycombDataStructure class contains a Honeycomb object and stores ThreeSidedDeque objects at each position in the honeycomb grid. It provides methods to set and get the deques at specific positions and to obtain the neighboring deques for a given position.

# Here's an example of how to use the HoneycombDataStructure class:


from honeycomb_data_structure import HoneycombDataStructure

def main():
    grid = HoneycombDataStructure(3, 3)
    deque_a = ThreeSidedDeque()
    deque_a.append_front(1)
    deque_a.append_middle(2)
    deque_a.append_back(3)

    deque_b = ThreeSidedDeque()
    deque_b.append_front(4)
    deque_b.append_middle(5)
    deque_b.append_back(6)

    grid.set(0, 0, deque_a)
    grid.set(1, 1, deque_b)

    print(grid)

    neighbors_a = grid.neighbors(0, 0)
    neighbors_b = grid.neighbors(1, 1)

    print("Neighbors of deque_a:")
    for neighbor in neighbors_a:
        print(neighbor)

    print("Neighbors of deque_b:")
    for neighbor in neighbors_b:
        print(neighbor)

if __name__ == "__main__":
    main()

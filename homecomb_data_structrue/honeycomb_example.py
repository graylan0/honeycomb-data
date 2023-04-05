from honeycomb import Honeycomb

def main():
    # Create a honeycomb grid with 4 rows and 6 columns
    grid = Honeycomb(4, 6)

    # Set some values in the honeycomb grid
    grid.set(0, 0, 'A')
    grid.set(1, 2, 'B')
    grid.set(2, 4, 'C')
    grid.set(3, 1, 'D')

    # Print the honeycomb grid
    print(grid)

    # Access values from the grid
    print("Value at (0, 0):", grid.get(0, 0))  # Output: A
    print("Value at (3, 1):", grid.get(3, 1))  # Output: D

    # Get neighbors of a cell
    neighbors = grid.neighbors(1, 2)
    print("Neighbors of (1, 2):", neighbors)  # Output: [None, None, 'A', 'C', None]

if __name__ == "__main__":
    main()

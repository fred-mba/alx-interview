#!/usr/bin/python3
"""Island perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid
       - 0 represents water 1 represents land
       - grid: is rectangular with its width and height not exceeding 100
       - Each cell is square, with a side length of 1
       - Cells are connected horizontally/vertically (not diagonally)
                     6
        ____________________________
       |                            |
       |     __1__                  |
       |     |   |                  |
       |     |___| 2                |
       |   3 |   |                  |5
       |     |___|____2____         |
       |     |   |    |    |  1     |
       |     |___|____|____| 	    |
       |            3               |
       |____________________________|
    """
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
            # Top is a land
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
            # Left is a land
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
    return perimeter

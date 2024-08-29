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
       |     |   |                  |
       |     |___| 2                |5
       |   3 |   |                  |
       |     |   |    2             |
       |     |___|__________        |
       |     |   |    |    |  1     |
       |     |___|____|____| 	    |
       |            3               |
       |____________________________|
    """
    perimeter = 0

    height = len(grid[0])
    length = len(grid)
    for col in range(height):
        for row in range(length):
            if grid[row][col] == 1:
                # Top
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Bottom
                if row == height-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # right
                if col == length-1 or grid[row][col+1] == 0:
                    perimeter += 1
    return perimeter

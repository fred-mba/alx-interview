## Island Perimeter
- An application knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context.
- The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

### Concepts Needed:
1. 2D Arrays (Matrices):

- Accessing and iterating over elements in a 2D array.
- Understanding how to navigate through adjacent cells (horizontally and vertically).
2. Conditional Logic:

- Applying conditions to determine whether a cell contributes to the perimeter of the island.
3. Counting Techniques:

- Developing a method to count the edges that contribute to the island’s perimeter.
4. Problem-Solving Strategies:

- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.
5. Python Programming:

- Nested loops for iterating over grid cells.
- Conditional statements to check the status of adjacent cells.

### Resources
1. Python Official Documentation:

- [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions): Understanding how to work with lists within lists in Python.
2. GeeksforGeeks Articles:

- [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): A guide to working with 2D arrays in Python effectively.
3. TutorialsPoint:

- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.
4. YouTube Tutorials:

- [Python 2D arrays and lists](https://www.youtube.com/watch?feature=shared&v=aNzepGawwCI)

### Explanation
- You need to calculate the perimeter by checking the neighbors of each land cell
1. perimeter = 0
2. Check top: If the current cell is at the top row (i == 0) or the cell above is water (grid[i-1][j] == 0), perimeter += 1
3. Check bottom: If the current cell is at the bottom row (i == rows-1) or the cell below is water (grid[i+1][j] == 0), perimeter += 1.
4. Check left: If the current cell is at the leftmost column (j == 0) or the cell to the left is water (grid[i][j-1] == 0), perimeter +=1.
5. Check right: If the current cell is at the rightmost column (j == cols-1) or the cell to the right is water (grid[i][j+1] == 0), perimeter += 1

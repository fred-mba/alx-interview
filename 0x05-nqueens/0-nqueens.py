#!/usr/bin/python3
"""
An implementation of N Queens problem using backtracking
"""
import sys


def solve_n_queens(n, cr=0, col=[], rd=[], ld=[]):
    """Solve N  Queens using backtracking and yield solutions.
       Parameters
       ----------
       n: a given number of queens on a nxn chessboard
       cr: the current row being processed
       rd: a list rep. the sums of rows and column for right diagonal
       ld: a list rep. differences of row and column indices for left diagonal
       col: list of column indices where queen are placed
    """
    if cr < n:
        for i in range(n):
            if i not in col and cr + i not in rd and cr - i not in ld:
                yield from solve_n_queens(
                    n, cr + 1, col + [i], rd + [cr + i], ld + [cr - i])
    else:
        yield col


def n_queens(n):
    """Solve n number of queens and print each solution.
    """
    for solution in solve_n_queens(n):
        print([[i, s] for i, s in enumerate(solution)])


def main():
    """Check for arguments and handle input validation
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens(n)


if __name__ == "__main__":
    main()

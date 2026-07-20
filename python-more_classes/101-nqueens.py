#!/usr/bin/python3
"""Solve the N Queens puzzle."""
import sys


def is_safe(queens, row, col):
    """Check if a queen can be placed at (row, col)."""
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, queens):
    """Solve the puzzle using backtracking."""
    if row == n:
        solution = []
        for r, c in enumerate(queens):
            solution.append([r, c])
        print(solution)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve(n, row + 1, queens)
            queens.pop()


def main():
    """Validate arguments and solve the puzzle."""
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

    solve(n, 0, [])


if __name__ == "__main__":
    main()

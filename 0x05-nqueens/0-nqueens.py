#!/usr/bin/python3

import sys

def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col:
                return False

        # Check diagonals
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i] == j:
                return False
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i] == j:
                return False

        return True

    def solve(board, row):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)

    result = []
    board = [-1] * n
    solve(board, 0)
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    result = nqueens(n)
    for solution in result:
        print([[i, j] for i, j in enumerate(solution)])

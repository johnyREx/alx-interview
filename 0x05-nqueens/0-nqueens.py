#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # check the column on the left
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_n_queens_util(board, col, N, solutions):
    if col == N:
        solutions.append(board[:])
        return

    for i in range(N):
        if is_safe(board, i, col):
            solve_n_queens_util(board, col + 1, N, solutions)
            board[col] = -1


def solve_n_queens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)

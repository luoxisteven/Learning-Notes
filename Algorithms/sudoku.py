def print_board(board):
    """Helper function to print the Sudoku board"""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def is_valid(board, row, col, num):
    """Check if placing a number on the board is valid"""
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 through 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):  # Recursively solve the rest of the board
                            return True

                        board[row][col] = 0  # Backtrack if the solution is invalid

                return False  # If no number fits, return False

    return True  # Return True if the board is completely solved


# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists!")

import math, random

class SudokuGenerator:
    # Initialize the Sudoku board with default parameters for row length and number of cells to remove
    def __init__(self, row_length=9, removed_cells=40):
        self.row_length = row_length  # Number of rows/columns in the board
        self.removed_cells = removed_cells  # Number of cells to remove to create the puzzle
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]  # Create a 2D list for the board
        self.box_length = int(math.sqrt(row_length))  # Size of the smaller boxes within the board

    # Return the current state of the board
    def get_board(self):
        return self.board

    # Print the current state of the board
    def print_board(self):
        for row in self.board:
            print(row)

    # Check if a number can be placed in the given row
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    # Check if a number can be placed in the given column
    def valid_in_col(self, col, num):
        return num not in [row[col] for row in self.board]

    # Check if a number can be placed in the 3x3 box
    def valid_in_box(self, row_start, col_start, num):
        row_start = (row_start // self.box_length) * self.box_length
        col_start = (col_start // self.box_length) * self.box_length
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    # Check if placing the number at a given position is valid
    def is_valid(self, row, col, num):
        return self.valid_in_box(row, col, num) and self.valid_in_col(col, num) and self.valid_in_row(row, num)

    # Fill a 3x3 box with numbers randomly
    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start + i][col_start + j] = nums.pop()

    # Fill all the diagonal 3x3 boxes in the Sudoku grid
    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    # Recursively fill all cells in the board starting from a given cell
    def fill_remaining(self, row, col):
        # If the end of a row is reached, move to the next row
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        # If the entire board is filled, return success
        if row >= self.row_length:
            return True
        # Adjust column index to skip over filled boxes
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        # Try all possible numbers in the current cell
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # Public method to start the board generation process
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # Remove a specified number of cells to create the puzzle
    def remove_cells(self):
        cells = [(i, j) for i in range(self.row_length) for j in range(self.row_length)]
        random.shuffle(cells)
        for _ in range(self.removed_cells):
            cell = cells.pop()
            self.board[cell[0]][cell[1]] = 0


# Function to generate a Sudoku puzzle
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

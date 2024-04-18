import math, random

class SudokuGenerator:
    '''
    create a sudoku board - initialize class variables and set up the 2D board
    This should initialize:
    self.row_length		- the length of each row
    self.removed_cells	- the total number of cells to be removed
    self.board			- a 2D list of ints to represent the board
    self.box_length		- the square root of row_length

    Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

    Return:
    None
    '''

    def __init__(self, row_length=9, removed_cells=40):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        # return num not in self.board[row]
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # return num not in [self.board[i][col] for i in range(self.row_length)]
        return num not in [row[col] for row in self.board]

    def valid_in_box(self, row_start, col_start, num):
        row_start = (row_start // 3) * 3
        col_start = (col_start // 3) * 3
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start+i][col_start+j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        # return (
        #     self.valid_in_row(row, num) and
        #     self.valid_in_col(col, num) and
        #     self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num)
        # )
        if self.valid_in_box(row, col, num) == True and self.valid_in_col(col, num) == True and self.valid_in_row(row,
                                                                                                                  num) == True:
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        # nums = list(range(1, self.box_length ** 2 + 1))
        # random.shuffle(nums)
        # for i in range(self.box_length):
        #     for j in range(self.box_length):
        #         self.board[row_start + i][col_start + j] = nums.pop()
        row_start = (row_start // 3) * 3
        col_start = (col_start // 3) * 3  # Zac 4/16: i implemented this just in case the wrong number is put so the full box is used
        for i in range(1, 10):  # runs the numbers 1-9
            if self.valid_in_box(row_start, col_start, i) == True:
                warn_count = 0
                while True:
                    slotx = random.randrange(0, 3)
                    sloty = random.randrange(0, 3)
                    if self.board[col_start + sloty][row_start + slotx] == 0:
                        self.board[col_start + sloty][row_start + slotx] = i
                        break

    def fill_diagonal(self):
        # for i in range(0, self.row_length, self.box_length):
        #     self.fill_box(i, i)
        for i in range(len(self.board)): #goes 9 times, one for each diagonal
            for l in range(self.box_length):  # goes 3 times, for each number
                while True: #creates loop until number filled
                    slotx = random.randrange(0, 3)
                    sloty = random.randrange(0, 3)
                    if self.board[3*l+sloty][3*l+slotx] == 0:
                        self.board[3*l+sloty][3*l + slotx] = i+1
                        break


    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
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

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        # cells_removed = 0
        # while cells_removed < self.removed_cells:
        #     row = random.randint(0, self.row_length - 1)
        #     col = random.randint(0, self.row_length - 1)
        #     if self.board[row][col] != 0:
        #         self.board[row][col] = 0
        #         cells_removed += 1
        for i in range(self.removed_cells):
            while True:
                slotx = random.randint(0, 8)
                sloty = random.randint(0, 8)
                if self.board[sloty][slotx] != 0:
                    self.board[sloty][slotx] = 0
                    break

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
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

        # Cesar: If soon could just confirm if that is correct ?? I think it is because I based it on the instructions
        # Zac 4/16: Ze this works perfectly with the filling diagonals and stuff.

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            print(row)

        # Cesar: This should print the board correctly
        # Zac 4/16: ye this is good

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        return num not in self.board[row]

        # Cesar: This should be all me need. I think this should check if 'num' is valid in the specified row
        # zac 4/16: ye this works perfectly

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        return num not in [row[col] for row in self.board]

    # Cesar: This should be all me need. Its like the row one. I dont think we need to do module. However its hard to test things
    # Zac 4/16: Ye this works it returns true or false

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        row_start = (row_start // 3) * 3
        col_start = (col_start // 3) * 3
        for i in range(self.box_length):  # checks the col 3 times
            for j in range(self.box_length):  # checks the row 3 times
                # if self.board[col_start+i][row_start+j] == num:
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    # Zac 4/16: i put some weird floor division and multiplication to make sure it actually starts at the box incase wrong number was put
    # Minh 4/18: I was having errors with changing the screens when it was line 100 instead of 101

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_box(row, col, num) == True and self.valid_in_col(col, num) == True and self.valid_in_row(row, num) == True:
            return True
        else:
            return False

    # Zac 4/16: should work

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        row_start = (row_start // 3) * 3
        col_start = (
                                col_start // 3) * 3  # Zac 4/16: i implemented this just in case the wrong number is put so the full box is used
        for i in range(1, 10):  # runs the numbers 1-9
            if self.valid_in_box(row_start, col_start, i) == True:
                warn_count = 0
                while True:
                    slotx = random.randrange(0, 3)
                    sloty = random.randrange(0, 3)
                    if self.board[col_start + sloty][row_start + slotx] == 0:
                        self.board[col_start + sloty][row_start + slotx] = i
                        break
            # zac 4/17: apparantly i overcomplicated it and i wasnt supossed to check if it matches with the row or column. SO i fixed it. seems simple.

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(len(self.board)):  # goes 9 times, one for each diagonal
            for l in range(self.box_length):  # goes 3 times, for each number
                while True:  # creates loop until number filled
                    slotx = random.randrange(0, 3)
                    sloty = random.randrange(0, 3)
                    if self.board[3 * l + sloty][3 * l + slotx] == 0:
                        self.board[3 * l + sloty][3 * l + slotx] = i + 1
                        break

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

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

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    # probably kist if mode = easy then rem = 30, medium rem = 40, hard rem = 50,
    # then have a while rem > 0:, pick random cell and if cell !=0, rem -= 1 and cell = 0
    def remove_cells(self):
        for i in range(self.removed_cells):
            while True:
                slotx = random.randint(0, 8)
                sloty = random.randint(0, 8)
                if self.board[sloty][slotx] != 0:
                    self.board[sloty][slotx] = 0
                    break

    '''
    DO NOT CHANGE
    Provided for students
    Given a number of rows and number of cells to remove, this function:
    1. creates a SudokuGenerator
    2. fills its values and saves this as the solved state
    3. removes the appropriate number of cells
    4. returns the representative 2D Python Lists of the board and solution

    Parameters:
    size is the number of rows/columns of the board (9 for this project)
    removed is the number of cells to clear (set to 0)

    Return: list[list] (a 2D Python list to represent the board)
    '''



def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

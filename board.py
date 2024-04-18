import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.removed_cells = 30 if difficulty == 'easy' else 40 if difficulty == 'medium' else 50
        self.generator = SudokuGenerator(9, self.removed_cells)
        self.generator.fill_values()
        self.board = self.generator.get_board()
        self.saved_board = ""
        for i in range(9):
            for j in range(9):
                self.saved_board += str(self.board[i][j])
        self.generator.remove_cells()
        self.selected_cell = None
        self.cells = [[Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)]

    '''Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board'''
    def draw(self):
        cell_size = self.width // 9
        for i in range(10):
            line_width = 2 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * cell_size), (self.width, i * cell_size), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, self.height), line_width)

        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

    '''Marks the cell at (row, col) in the board as the current selected cell. Once a cell has been selected, the user can edit its value or sketched value'''
    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        row = y // (self.height // 9)
        col = x // (self.width // 9)
        if 0 <= row < 9 and 0 <= col < 9:
            self.select(row, col)
    '''If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None.'''

    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell.row, self.selected_cell.col
            if self.board[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(0)
    '''Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    filled by themselves.'''
    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell.row, self.selected_cell.col
            self.cells[row][col].set_sketched_value(value)
    '''Sets the sketched value of the current selected cell equal to user entered value. It will be displayed at the top left corner of the cell using the draw() function.'''

    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell.row, self.selected_cell.col
            if self.board[row][col] == 0:
                self.cells[row][col].set_cell_value(value)
    '''Sets the value of the current selected cell equal to user entered value. Called when the user presses the Enter key.'''

    def reset_to_original(self):
        self.generator = SudokuGenerator(9, self.removed_cells)
        self.generator.fill_values()
        self.board = self.generator.get_board()
        self.generator.remove_cells()
        self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
    '''Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).'''

    def is_full(self):
        return all(cell.value != 0 for row in self.cells for cell in row)
    '''Returns a Boolean value indicating whether the board is full or not.'''

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value
    '''Updates the underlying 2D board with the values in all cells.'''

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None
    '''Finds an empty cell and returns its row and col as a tuple (x, y).'''

    def check_board(self):
        check_answer = ""
        for i in range(9):
            for j in range(9):
                check_answer += str(self.board[i][j])
        if self.saved_board == check_answer:
            return True
        else:
            return False
        #Zac 4/18: should work
    '''Check whether the Sudoku board is solved correctly.'''

python sudoku.py

from sudoku_generator import *

my_sudoku = SudokuGenerator()
my_sudoku.fill_diagonal()
my_sudoku.print_board()
print()
print("starting")
print()
my_sudoku.fill_box(3,0)
# my_sudoku.fill_values()
my_sudoku.print_board()

#Zac 4/17: above is an example of starting a sudoku game, filling idagonals, and filling a square with random numbers. it all seems to work fine


'''In addition to the above classes, students will have a sudoku.py file, where the main function will be run. This
file will contain code to create the different screens of the project (game start, game over, and game in
progress), and will form a cohesive project together with the rest of the code'''

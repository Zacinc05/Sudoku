import pygame
from board import Board
pygame.init()

# setting up the screen
width = 540
height = 600
WINDOW_SIZE = (width, height)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku")

# Colors and font
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.Font(None, 36)

# Game states
STATE_START = 0
STATE_PLAYING = 1
STATE_WIN = 2
STATE_LOSE = 3
game_state = STATE_START

# Game difficulty and board
difficulty = None
board = None

# Draw the Game Start screen
def draw_start_screen(): 

    """
    Draw the start screen and handle difficulty selection.
    Returns the selected difficulty.
    """

    bg = pygame.image.load('sudokupic.png')
    size = pygame.transform.scale(bg, (540, 800))
    screen.blit(size, (0, 0))

    #Yasser:
    #4/22 Ran general testing again. #Add background splash to initial screen too

    title = FONT.render("Welcome to Sudoku", True, BLACK)
    title_rect = title.get_rect(center=(width // 2, height // 4))
    screen.blit(title, title_rect)

    easy_button = pygame.Rect(width // 10, height // 2, width // 4, 50)
    medium_button = pygame.Rect(width // 2 - width // 8, height // 2, width // 4, 50)
    hard_button = pygame.Rect(3 * width // 4 - width // 10, height // 2, width // 4, 50)

    pygame.draw.rect(screen, GREEN, easy_button)
    pygame.draw.rect(screen, GREEN, medium_button)
    pygame.draw.rect(screen, GREEN, hard_button)

    easy_text = FONT.render("Easy", True, BLACK)
    medium_text = FONT.render("Medium", True, BLACK)
    hard_text = FONT.render("Hard", True, BLACK)

    easy_text_rect = easy_text.get_rect(center=easy_button.center)
    medium_text_rect = medium_text.get_rect(center=medium_button.center)
    hard_text_rect = hard_text.get_rect(center=hard_button.center)

    screen.blit(easy_text, easy_text_rect)
    screen.blit(medium_text, medium_text_rect)
    screen.blit(hard_text, hard_text_rect)

    pygame.display.update()

    # Wait for button click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(mouse_pos):
                    return 'easy'
                elif medium_button.collidepoint(mouse_pos):
                    return 'medium'
                elif hard_button.collidepoint(mouse_pos):
                    return 'hard'

# Draw the Game In Progress screen
def draw_game_screen(): #minh: all buttons should work properly
    screen.fill(WHITE)
    board.draw()

    reset_button = pygame.Rect(width // 4 - 50, height - 50, 100, 40)
    restart_button = pygame.Rect(width // 2 - 50, height - 50, 100, 40)
    exit_button = pygame.Rect(3 * width // 4 - 50, height - 50, 100, 40)

    pygame.draw.rect(screen, GREEN, reset_button)
    pygame.draw.rect(screen, GREEN, restart_button)
    pygame.draw.rect(screen, RED, exit_button)

    reset_text = FONT.render("Reset", True, BLACK)
    restart_text = FONT.render("Restart", True, BLACK)
    exit_text = FONT.render("Exit", True, BLACK)

    reset_text_rect = reset_text.get_rect(center=reset_button.center)
    restart_text_rect = restart_text.get_rect(center=restart_button.center)
    exit_text_rect = exit_text.get_rect(center=exit_button.center)

    screen.blit(reset_text, reset_text_rect)
    screen.blit(restart_text, restart_text_rect)
    screen.blit(exit_text, exit_text_rect)

    pygame.display.update()

# Draw the Game Won screen
def draw_win_screen():
    bg = pygame.image.load('sudokupic.png')
    size = pygame.transform.scale(bg, (540, 800))
    screen.blit(size, (0, 0))

    #Yasser 4/18: Instead of a blank white a custom background is applied

    win_text = FONT.render("Game Won!", True, GREEN)
    win_rect = win_text.get_rect(center=(width // 2, height // 2))
    screen.blit(win_text, win_rect)

    exit_button = pygame.Rect(width // 2 - 50, 3 * height // 4, 100, 50)
    pygame.draw.rect(screen, RED, exit_button)
    exit_text = FONT.render("Exit", True, BLACK)
    exit_rect = exit_text.get_rect(center=exit_button.center)
    screen.blit(exit_text, exit_rect)
    pygame.display.update()

# Draw the Game Over screen
def draw_lose_screen(): #minh: should show up with buttons working properly, only problem is check_board()
    bg = pygame.image.load('sudokupic.png')
    size = pygame.transform.scale(bg, (540, 800))
    screen.blit(size, (0, 0))

    # Yasser 4/18: Instead of a blank white a custom background is applied

    lose_text = FONT.render("Game Over", True, RED)
    lose_rect = lose_text.get_rect(center=(width // 2, height // 2))
    screen.blit(lose_text, lose_rect)

    restart_button = pygame.Rect(width // 2 - 100, 3 * height // 4, 100, 50)
    exit_button = pygame.Rect(width // 2 + 10, 3 * height // 4, 100, 50)
    pygame.draw.rect(screen, GREEN, restart_button)
    pygame.draw.rect(screen, RED, exit_button)
    restart_text = FONT.render("Restart", True, BLACK)
    exit_text = FONT.render("Exit", True, BLACK)
    restart_rect = restart_text.get_rect(center=restart_button.center)
    exit_rect = exit_text.get_rect(center=exit_button.center)
    screen.blit(restart_text, restart_rect)
    screen.blit(exit_text, exit_rect)

    pygame.display.update()

# Game loop
running = True
while running:
    difficulty = draw_start_screen()
    board = Board(width, height - 60, screen, difficulty)
    game_state = STATE_PLAYING

    # Main game loop
    while game_state == STATE_PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user quits, end the game
                running = False
                game_state = STATE_LOSE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[1] < height - 60:
                        # If the click is on the board, handle it
                        board.click(*pos)
                    else:
                        # If the click is on a button, handle it
                        if width // 4 - 50 <= pos[0] <= width // 4 + 50 and height - 50 <= pos[1] <= height - 10:
                            board.reset_to_original()
                        elif width // 2 - 50 <= pos[0] <= width // 2 + 50 and height - 50 <= pos[1] <= height - 10:
                            game_state = STATE_START
                        elif 3 * width // 4 - 50 <= pos[0] <= 3 * width // 4 + 50 and height - 50 <= pos[1] <= height - 10:
                            running = False
                            game_state = STATE_LOSE
            elif event.type == pygame.KEYDOWN:
                # Handle key presses for sketching, placing numbers, and navigating the board
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    board.sketch(1)
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    board.sketch(2)
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    board.sketch(3)
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    board.sketch(4)
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    board.sketch(5)
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    board.sketch(6)
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    board.sketch(7)
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    board.sketch(8)
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    board.sketch(9)
                elif event.key == pygame.K_RETURN:

                #Cesar added num pad support
                    if board.selected_cell:
                        row, col = board.selected_cell.row, board.selected_cell.col
                        board.place_number(board.cells[row][col].sketched_value)
                        board.update_board()

                    #minh: if you try pressing enter to place a number into an empty cell, it should work properly
                    #i believe the code below should work properly too based on how it look, but I haven't
                    #gotten to check_board() in board.py yet, maybe you guys could look over that for me

                        if board.is_full():
                            if board.check_board():
                                game_state = STATE_WIN
                            else:
                                game_state = STATE_LOSE

                elif event.key == pygame.K_DELETE:
                    board.clear()
                elif event.key == pygame.K_UP:
                    if board.selected_cell:
                        row, col = board.selected_cell.row, board.selected_cell.col
                        if row > 0:
                            board.select(row - 1, col)
                elif event.key == pygame.K_DOWN:
                    if board.selected_cell:
                        row, col = board.selected_cell.row, board.selected_cell.col
                        if row < 8:
                            board.select(row + 1, col)
                elif event.key == pygame.K_LEFT:
                    if board.selected_cell:
                        row, col = board.selected_cell.row, board.selected_cell.col
                        if col > 0:
                            board.select(row, col - 1)
                elif event.key == pygame.K_RIGHT:
                    if board.selected_cell:
                        row, col = board.selected_cell.row, board.selected_cell.col
                        if col < 8:
                            board.select(row, col + 1)
        # Update the game screen
        draw_game_screen()


    # Game over, check if win or lose
    if game_state == STATE_WIN:
        draw_win_screen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    exit_button = pygame.Rect(width // 2 - 50, 3 * height // 4, 100, 50)
                    if exit_button.collidepoint(mouse_pos):
                        running = False
                        break
            if not running:
                break

    elif game_state == STATE_LOSE:
        draw_lose_screen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    restart_button = pygame.Rect(width // 2 - 100, 3 * height // 4, 100, 50)
                    exit_button = pygame.Rect(width // 2 + 10, 3 * height // 4, 100, 50)
                    if restart_button.collidepoint(mouse_pos):
                        game_state = STATE_PLAYING
                        board.reset_to_original()
                        break
                    elif exit_button.collidepoint(mouse_pos):
                        running = False
                        break
            if game_state == STATE_PLAYING or not running:
                break
            
# Quit the game
pygame.quit()
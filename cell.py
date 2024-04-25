import pygame

class Cell:
    #constants
    FONT_SIZE = 36
    SKETCHED_FONT_SIZE = 30
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    RED = (255, 0, 0)

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.cell_size = screen.get_width() // 9  # Assume a 9x9 grid for simplicity
        # Load font once instead of every draw call
        self.font = pygame.font.Font(None, Cell.FONT_SIZE)
        self.sketched_font = pygame.font.Font(None, Cell.SKETCHED_FONT_SIZE)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        # Define the rectangle for the cell
        cell_rect = pygame.Rect(self.col * self.cell_size, self.row * self.cell_size, self.cell_size, self.cell_size)
        # Draw the rectangle outline
        pygame.draw.rect(self.screen, Cell.BLACK, cell_rect, 1)

        # Drawing the main value of the cell if it is not zero
        if self.value != 0:
            text = self.font.render(str(self.value), True, Cell.BLACK)
            text_rect = text.get_rect(center=cell_rect.center)
            self.screen.blit(text, text_rect)
        # If the main value is zero, possibly draw a sketched value
        elif self.sketched_value != 0:
            text = self.sketched_font.render(str(self.sketched_value), True, Cell.GRAY)
            text_rect = text.get_rect(topleft=(cell_rect.left + 5, cell_rect.top + 5))
            self.screen.blit(text, text_rect)

        # Highlight the cell if it is selected
        if self.selected:
            pygame.draw.rect(self.screen, Cell.RED, cell_rect, 2)


#Cesar 4/18: Added comments and made it so its easy to chance values.

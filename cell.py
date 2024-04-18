import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    # def draw(self):
    #     cell_size = self.screen.get_width() // 9
    #     cell_rect = pygame.Rect(self.col * cell_size, self.row * cell_size, cell_size, cell_size)
    #     pygame.draw.rect(self.screen, (255, 255, 255), cell_rect)
    #
    #     if self.value != 0:
    #         font = pygame.font.Font(None, 36)
    #         text = font.render(str(self.value), True, (0, 0, 0))
    #         text_rect = text.get_rect(center=cell_rect.center)
    #         self.screen.blit(text, text_rect)
    #
    #     if self.selected:
    #         pygame.draw.rect(self.screen, (255, 0, 0), cell_rect, 2)

    def draw(self):
        cell_size = self.screen.get_width() // 9
        cell_rect = pygame.Rect(self.col * cell_size, self.row * cell_size, cell_size, cell_size)
        pygame.draw.rect(self.screen, (0, 0, 0), cell_rect, 1)

        if self.value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=cell_rect.center)
            self.screen.blit(text, text_rect)
        elif self.sketched_value != 0:
            font = pygame.font.Font(None, 30)
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            text_rect = text.get_rect(topleft=(cell_rect.left + 5, cell_rect.top + 5))
            self.screen.blit(text, text_rect)

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), cell_rect, 2)
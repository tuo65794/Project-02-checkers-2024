import pygame
from constants import SQUARE_SIZE

class pieces:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.king = False  

    def draw(self, win):
  
        radius = SQUARE_SIZE // 2 - 5
        x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

        pygame.draw.circle(win, self.color, (x, y), radius)

    def move(self, new_row, new_col):
  
        self.row = new_row
        self.col = new_col

    def make_king(self):
  
        self.king = True

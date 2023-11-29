import pygame
from constants import SQUARE_SIZE

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.king = False  
        self.calc_pos()
         
    def calc_pos(self):
          self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
          self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
  
        radius = SQUARE_SIZE // 2 - 5
        x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

        pygame.draw.circle(win, self.color, (x, y), radius)

    def move(self, new_row, new_col):
  
        self.row = new_row
        self.col = new_col
        self.calc_pos()
        

    def make_king(self):
  
        self.king = True

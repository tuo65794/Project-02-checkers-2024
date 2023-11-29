import pygame
from constants import RED, BLACK, SQUARE_SIZE
from pieces import Piece

ROWS = 8

class MAIN_Board:
    def __init__(self, color1, color2, board_color):
        self.color1 = color1
        self.color2 = color2
        self.board_color = board_color
        self.board = [[None] * ROWS for _ in range(ROWS)]
        self.initialize_pieces()

    def initialize_pieces(self):
        # Place initial pieces on the board
        for row in range(3):
            for col in range(ROWS):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Piece(self.color1, row, col)

        for row in range(5, ROWS):
            for col in range(ROWS):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Piece(self.color2, row, col)

    def draw_board(self, win):
        win.fill(self.board_color)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                #This draws the board color 
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            for col in range((row + 1) % 2, ROWS, 2):
                #This draws the board color 
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, win):
        for row in range(ROWS):
            for col in range(ROWS):
                piece = self.board[row][col]
                if piece:
                    piece.draw(win)

    def place_piece(self, row, col, piece):
        self.board[row][col] = piece

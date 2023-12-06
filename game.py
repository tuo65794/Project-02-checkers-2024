# game.py
# game file that holds game logic, game class has Main_Board object
# code from reference repo: https://github.com/techwithtim/Python-Checkers-AI

import pygame
from constants import RED, WHITE, YELLOW, SQUARE_SIZE
from Main_Board import Main_Board

class Game: # game class to handle game logic, color represents board color chosen by user
    def __init__(self, win, color, player1, player2):
        self.turn_start_time = pygame.time.get_ticks()
        self.turn_timeout = 5200  # 5.2 seconds per turn
        self.win = win
        self.color = color
        self.selected = None
        self.board = Main_Board(self.color)
        self.turn = RED
        self.valid_moves = {}
        self.font = pygame.font.Font(None, 36)  # Font for rendering text
        self.text_color = WHITE  # Text color
        self.text_urgent_color = RED  # Text color when time is running out
        self.screen = pygame.display.set_mode((1000, 700))
        self.player1 = player1
        self.player2 = player2
        
    def check_turn_timeout(self):
        elapsed_time = pygame.time.get_ticks() - self.turn_start_time
        elapsed_seconds = elapsed_time // 1000 
        text = f"Move Timer: {elapsed_seconds} s"
        text_surface = self.font.render(text, True, self.text_color)
        if elapsed_time > 3000:
            text_surface = self.font.render(text, True, self.text_urgent_color)
        else:
            text_surface = self.font.render(text, True, self.text_color)
        # Render text
        self.screen.blit(text_surface, (715, 50))
        if elapsed_time > self.turn_timeout:
            self.change_turn()

    def display_turn(self): # display whose turn on screen
        if self.turn == RED:
            text = f"Current Turn: RED"
        else:
            text = f"Current Turn: WHITE"
        text_surface = self.font.render(text, True, self.text_color)
        self.screen.blit(text_surface, (715, 100))

    def display_piece_count(self): # display piece count on screen
        text = f"RED Pieces Left: {self.board.red_left}"
        text2 = f"WHITE Pieces Left: {self.board.white_left}"
        text_surface = self.font.render(text, True, self.text_color)
        text_surface2 = self.font.render(text2, True, self.text_color)
        self.screen.blit(text_surface, (715, 150))
        self.screen.blit(text_surface2, (715, 200))

    def display_player_names(self, player1, player2): # display player names on screen
        text = f"Player 1: {player1}"
        text2 = f"Player 2: {player2}"
        text_surface = self.font.render(text, True, self.text_color)
        text_surface2 = self.font.render(text2, True, self.text_color)
        self.screen.blit(text_surface, (715, 350))
        self.screen.blit(text_surface2, (715, 400))

    def update(self): # update board to show current board and features
        self.board.draw(self.win)
        self.show_available_moves(self.valid_moves)
        self.check_turn_timeout()
        self.display_turn()
        self.display_piece_count()
        self.display_player_names(self.player1, self.player2)
        pygame.display.update()
        
    def winner(self): # if winner has been found, return winner
        return self.board.winner()

    def select(self, row, col): # select piece to move and as a result show available moves
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        try:# this try catch must be here when user click outside board
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        except:# future problem can arise when clicking back to menu button
            return None
            
        return False

    def move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves.get((row, col))
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            self.turn_start_time = pygame.time.get_ticks()  # Reset the turn timer
            return True

        return False

    def show_available_moves(self, moves): # show available moves for selected piece
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self): # change turn to other player/color
        self.valid_moves = {}
        self.turn_start_time = pygame.time.get_ticks()  # Reset the turn timer
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self): # return current board
        return self.board

    def ai_move(self, board): # move AI piece
        self.board = board
        self.change_turn()
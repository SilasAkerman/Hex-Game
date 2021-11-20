import pygame

from .board import Board
from .tile import Tile

class HexGame:
     BACKGROUND = (200, 200, 150)
     LEFT_START = True

     FONT = pygame.font.Font("freesansbold.ttf", 35)

     UNDO_COUNTER = -1

     def __init__(self):
          self.board = Board()
          self.left_turn = self.LEFT_START
          self.winner = False

          self.moves = []
          self.undoos = 0
     
     def display(self, win):
          win.fill(self.BACKGROUND)
          self.board.display(win)
          if self.winner:
               self.display_winner(win)
          self.display_turn(win)
          pygame.display.update()
     
     def display_winner(self, win):
          text = self.FONT.render(f"Team {str(self.winner)} wins!!!", True, (0, 0, 0))
          win.blit(text, (70, win.get_height() - 70))

     def display_turn(self, win):
          color = self.board.TEAM_1_COLOR if self.left_turn else self.board.TEAM_2_COLOR
          turn_tile = Tile((win.get_width()-50, 50), self.board.TILE_SIZE, color)
          turn_tile.display(win, (-1, -1))


     def make_move(self, spot):
          team = 1 if self.left_turn else 2
          self.moves.append(spot)
          self.place(spot, team)
          self.alternate_turns()
          self.check_winner()
          self.undoos = 0
     
     def undo(self):
          if len(self.moves) <= 0 or (self.undoos >= self.UNDO_COUNTER and not self.UNDO_COUNTER < 0):
               return
          team = 1 if self.left_turn else 2
          spot = self.moves[-1]
          self.moves.pop()
          self.board.undo(spot)
          self.alternate_turns()
          self.check_winner()
          self.undoos += 1

     def place(self, spot, team):
          self.board.place(spot, team)
     
     def alternate_turns(self):
          self.left_turn = 1 - self.left_turn
     
     def check_winner(self):
          self.winner = self.board.check_winner()
     
     def get_row_col_from_mouse(self, mouse_coords):
          return self.board.get_row_col_from_mouse(mouse_coords)
import pygame
import math

from .tile import Tile

class Board:
     SIZE = 10 + 2 # This also counts the edges
     TEAM_1_COLOR = (0, 0, 255)
     TEAM_2_COLOR = (255, 0, 0)

     TOP_LEFT = (45, 45)
     TILE_SIZE = 40

     def __init__(self):
          self._init_tiles()

     def _init_tiles(self):
          self.board = [[None for _ in range(self.SIZE)] for _ in range(self.SIZE)]

          for row in range(self.SIZE):
               for col in range(self.SIZE):
                    location = (self.TOP_LEFT[0] + col*(math.sin(math.pi/3)*self.TILE_SIZE*2) + row*(math.sin(math.pi/3)*self.TILE_SIZE), 
                                self.TOP_LEFT[1] + row*(math.cos(math.pi/3)*self.TILE_SIZE + self.TILE_SIZE))

                    if (row, col) == (0, 0) or (row, col) == (self.SIZE-1, 0) or (row, col) == (0, self.SIZE-1) or (row, col) == (self.SIZE-1, self.SIZE-1):
                         self.board[row][col] = None
                         continue
                    
                    if row == 0 or row == self.SIZE-1:
                         self.board[row][col] = Tile(location, self.TILE_SIZE, self.TEAM_2_COLOR)
                         continue
                    if col == 0 or col == self.SIZE-1:
                         self.board[row][col] = Tile(location, self.TILE_SIZE, self.TEAM_1_COLOR)
                         continue

                    self.board[row][col] = Tile(location, self.TILE_SIZE)
     
     
     def display(self, win):
          for row in range(self.SIZE):
               for col in range(self.SIZE):
                    if self.board[row][col] is None:
                         continue
                    self.board[row][col].display(win, (row, col))

     def place(self, spot, team):
          color = self.TEAM_1_COLOR if team == 1 else self.TEAM_2_COLOR
          self.board[spot[0]][spot[1]].place(color)
     
     def undo(self, spot):
          self.board[spot[0]][spot[1]].place((100, 100, 100))
     

     def check_winner(self):
          if self._check_color_win(self.TEAM_1_COLOR):
               return 1
          if self._check_color_win(self.TEAM_2_COLOR):
               return 2
          return False

     def _check_color_win(self, color):
          horizontal = True if color == self.TEAM_1_COLOR else False
          if horizontal:
               starting = set((i, 0) for i in range(1, self.SIZE-1))
          else:
               starting = set((0, i) for i in range(1, self.SIZE-1))
          
          for spot in starting.copy():
               if self._check_piece_path(spot, starting, horizontal):
                    return True
          return False

     def _check_piece_path(self, spot, searched, horizontal):
          surroundings = {
               (spot[0], spot[1]-1),
               (spot[0]+1, spot[1]-1),
               (spot[0]-1, spot[1]),
               (spot[0]+1, spot[1]),
               (spot[0]-1, spot[1]+1),
               (spot[0], spot[1]+1)
          }
          if horizontal:
               winning = set((i, self.SIZE-1) for i in range(1, self.SIZE-1))
          else:
               winning = set((self.SIZE-1, i) for i in range(1, self.SIZE-1))

          for place in surroundings:
               if place in winning:
                    return True
               if place[0] < 0 or place[0] >= self.SIZE-1 or place[1] < 0 or place[1] >= self.SIZE-1:
                    continue
               if place == (0, 0) or place == (self.SIZE-1, 0) or place == (0, self.SIZE-1) or place == (self.SIZE-1, self.SIZE-1):
                    continue
               if place in searched:
                    continue

               searched.add(place)

               if self.board[place[0]][place[1]].color == self.board[spot[0]][spot[1]].color:
                    if self._check_piece_path(place, searched, horizontal):
                         return True

          return False
          
     
     def get_row_col_from_mouse(self, mouse_coords):
          for row in range(1, self.SIZE-1): # Skip the edges
               for col in range(1, self.SIZE-1):
                    tile = self.board[row][col]
                    if tile.color == self.TEAM_1_COLOR or tile.color == self.TEAM_2_COLOR: # Can't select a placed tile
                         continue
                    if tile.distance(mouse_coords) < tile.circle_size:
                         return row, col
          return False
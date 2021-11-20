import random

def random_move(board):
     options = []
     for row in range(board.SIZE):
          for col in range(board.SIZE):
               tile = board.board[row][col]
               if tile is None:
                    continue
               if not (tile.color == board.TEAM_1_COLOR or tile.color == board.TEAM_2_COLOR):
                    options.append((row, col))
     
     return random.choice(options)
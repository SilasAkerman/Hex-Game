import pygame
import sys

from Hex.game import HexGame
from Hex.random_player import random_move

WIN_WIDTH = 1200
WIN_HEIGHT = 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

FPS = 30

RANDOM_1 = False
RADNOM_2 = False


def main():
     clock = pygame.time.Clock()
     Game = HexGame()

     run = True
     while run:
          clock.tick(FPS)

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                         pygame.quit()
                         sys.exit()
                    
                    if event.key == pygame.K_r:
                         Game = HexGame()
                    if event.key == pygame.K_b:
                         Game.undo()
               
               if event.type == pygame.MOUSEBUTTONDOWN and not Game.winner and not((RANDOM_1 and Game.left_turn) or (RADNOM_2 and not Game.left_turn)):
                    spot = Game.get_row_col_from_mouse(pygame.mouse.get_pos())
                    if spot:
                         Game.make_move(spot)
          
          if ((RANDOM_1 and Game.left_turn) or (RADNOM_2 and not Game.left_turn)) and not Game.winner:
               Game.make_move(random_move(Game.board))
          
          Game.display(WIN)



if __name__ == "__main__":
     main()
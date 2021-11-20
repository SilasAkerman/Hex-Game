import pygame
import math

class Tile:
     pygame.init()
     
     WIDTH = 2
     FREE_TILE_COLOR = (100, 100, 100)
     OUTLINE_COLOR = (0, 0, 0)

     FONT = pygame.font.Font("freesansbold.ttf", 16)

     def __init__(self, location, size, color=FREE_TILE_COLOR):
          self.location = pygame.Vector2(location)
          self.size = size
          self.color = color

          self._init_vertecies()
          self._init_hitbox()

     def _init_vertecies(self):
          self.vertecies = []
          starting_vertex = pygame.Vector2(0, self.size)
          for i in range(6):
               self.vertecies.append(starting_vertex + self.location)
               starting_vertex.rotate_ip_rad(math.pi/3)
          
     def _init_hitbox(self):
          self.circle_size = math.sin(math.pi/3) * self.size
     
     def place(self, color):
          self.color = color
     
     def distance(self, coords):
          distance = math.sqrt((self.location.x - coords[0])**2 + (self.location.y - coords[1])**2)
          return distance
     
     def display(self, win, spot):
          pygame.draw.polygon(win, self.color, self.vertecies)
          pygame.draw.polygon(win, self.OUTLINE_COLOR, self.vertecies, self.WIDTH)
          text = self.FONT.render(str(spot), True, (0, 0, 0))
          # win.blit(text, (self.location.x - text.get_width()/2, self.location.y))
          # pygame.draw.circle(win, self.OUTLINE_COLOR, self.location, self.circle_size, self.WIDTH)
          # pygame.draw.rect(win, self.OUTLINE_COLOR, (self.location.x-self.size, self.location.y-self.size, self.size*2, self.size*2), self.WIDTH)
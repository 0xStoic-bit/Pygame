#First terminal install pygame(pip install pygame)

import pygame
import sys

Widht = 600
Height = 400

# İF you want to computer screen equal pygame screen use this code !!
#ekran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#Genislik, Yukseklik = ekran.get_size()


screen = pygame.display.set_mode((Widht,Height))

state = True
while state:
  for event in pygame.event.get():
    if even.type == pygame.QUIT:
      state = False

pygame.quit()
sys.exit()

#Basic screen opening the phython phycharm library.

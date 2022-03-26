import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()
test = pygame.Surface((300, 200))
test.fill('Red')

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.blit(test, (0, 0))
  pygame.display.update()
  clock.tick(60)

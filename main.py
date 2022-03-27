import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()
bg = pygame.Surface((800, 400))
ground = pygame.Surface((800, 200))
bg.fill('blue')
ground.fill('green')

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.blit(bg, (0, 0))
  screen.blit(ground, (0, 300))
  pygame.display.update()
  clock.tick(60)

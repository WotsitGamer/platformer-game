import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()
bg = pygame.Surface((800, 400))
ground = pygame.Surface((800, 200))
font = pygame.font.Font('font/nova.ttf', 30)
enemy = pygame.Surface((50, 50))
enemyOriginalX = 600
enemyOriginalY = 250
enemySpeed = 4

bg.fill('blue')
ground.fill('green')
title = font.render('Platformer Game', False, 'yellow')
enemy.fill('purple')


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.blit(bg, (0, 0))
  screen.blit(ground, (0, 300))
  screen.blit(title, (275, 50))
  screen.blit(enemy,(enemyOriginalX, enemyOriginalY))
  pygame.display.update()
  enemyOriginalX -= enemySpeed
  if enemyOriginalX < -100:
    enemyOriginalX = 800
  clock.tick(60)

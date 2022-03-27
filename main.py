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
player = pygame.Surface((50, 100))

enemyOriginalX = 600
enemyOriginalY = 250
enemySpeed = 4
enemy_rect = enemy.get_rect(topleft = (enemyOriginalX, enemyOriginalY))
player_rect = player.get_rect(topleft = (20, 200))

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
  screen.blit(enemy, enemy_rect)
  screen.blit(player, player_rect)
  enemy_rect.x -= enemySpeed
  if enemy_rect.right <= 0: enemy_rect.left = 800

  #if player_rect.colliderect(enemy_rect):
    #print('epic')
  mouse_pos = pygame.mouse.get_pos()
  if player_rect.collidepoint((mouse_pos)):
    print(pygame.mouse.get_pressed())

  pygame.display.update()
  clock.tick(60)

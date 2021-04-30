import pygame
import random
pygame.init()

#variables
FPS = 60
WIDTH = 600
HEIGHT = 500
xpos = 200
ypos = 100
border = 20,20

PINK = (139,0,139)

#anything above loop
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

Maze = []

#game loop---------------------------------------------------
stop = False

while not stop:
  clock.tick(FPS)

  #keyboard input
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          done = True 
  
  keys = pygame.key.get_pressed() 
  if keys[pygame.K_UP]:
    ypos -= 5
  if keys[pygame.K_DOWN]:
    ypos += 5
  if keys[pygame.K_LEFT]:
    xpos -= 5
  if keys[pygame.K_RIGHT]:
    xpos += 5

  #game logic-------------------------------------------------

  #render section-----------------------------------------------
  screen.fill((0,0,0))

  pygame.draw.rect(screen, PINK, (xpos,ypos,20,20))





  pygame.display.flip()

pygame.quit()#end of loop
import pygame
import random
pygame.init()

#variables
FPS = 60
WIDTH = 600
HEIGHT = 500
xpos = 200
ypos = 100
pW = 20
pH = 20
  #velocities
pVx = 0
pVy = 0


#CONSTANTS
PINK = (139,0,139)
RIGHT = 0
LEFT =1
UP = 2
DOWN =3

direction = RIGHT

#anything above loop
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class maze:
  def __init__ (self):
    self.Maze = [[0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0]]

  def draw(self):
    #maze map

    for i in range (10):
      for j in range (12):
        if self.Maze[i][j]==1:
          pygame.draw.rect(screen, (255,0,0), (j*50,i*50,50,50))
        else:
          pygame.draw.rect(screen, (255,255,255), (j*50,i*50,50,50), 1)

  def collide (self,px, py, direction):

    if direction is RIGHT:
          #print("checking ", px, " , ",py, "and row/column", px/50, " , ",py/50)
          if self.Maze[int(py/50)][int((px+20)/50)]==1:
           print("collision from right!")
           return True
          else:
            print("no collision")

m1 = maze()

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
    pVy = -2
  elif keys[pygame.K_DOWN]:
    pVy = 2
  else:
    pVy = 0

  if keys[pygame.K_LEFT]:
    pVx = -2
  elif keys[pygame.K_RIGHT]:
    pVx = 2
  else:
    pVx = 0

  #game logic-------------------------------------------------
  if pVy > 0:
    direction = DOWN
  if pVy <0:
    direction = UP
  if pVx <0:
    direction = LEFT
  if pVx>0:
    direction = RIGHT



  if m1.collide(xpos, ypos, direction)== True:
    print("collsion!")
    if direction == RIGHT or direction  == LEFT:
      pVx *=-1

  xpos += pVx
  ypos += pVy

  #render section-----------------------------------------------
  screen.fill((0,0,0))

  #for i in range (10): # 
    #for j in range (12):
      #if Maze[i][j]==1:
        #wall = pygame.draw.rect(screen, (255,0,0), (j*50,i*50,50,50))#(top left x, top left y, width, height)
      #if GameMap[i][j]==2:
        #pygame.draw.rect(screen, (255,255,0), (j*25,i*25,25,25))#(top left x, top left y, width, height)
      #if GameMap[i][j]==3:
        #pygame.draw.rect(screen, (0,255,0), (j*25,i*25,25,25))#(top left x, top left y, width, height)


  player = pygame.draw.rect(screen, PINK, (xpos,ypos,pW,pH))
  m1.draw()
  #player.center = (xpos+20, ypos+20)
  #collide = wall.colliderect(player)
  #if collide:
    #print("collision...v")
    #print("collision...^")
    #xpos -= .5
    #ypos -= .5
    

  


  pygame.display.flip()

pygame.quit()#end of loop
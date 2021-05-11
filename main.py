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

#gamestates stuff
START = 0
PLAYING = 1#level 1
LEVEL2 = 2

PLAY = 0
PAUSE = 1
QUIT = 2
LEFT = 3
RIGHT = 4
UP = 5
DOWN = 6
PLAY2 = 7

game_state = START

state = [False, False, False, False, False, False, False, False, False]


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
    self.Maze = [[1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,1,1,0,1,1,1,1,1,0,1],
          [1,0,0,0,9,0,1,0,0,0,0,1],
          [0,1,1,0,1,0,1,0,1,1,0,1],
          [1,0,1,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,1],
          [1,0,0,0,1,0,1,0,1,1,1,1],
          [1,0,1,1,0,0,0,1,1,1,0,1],
          [1,0,0,0,1,1,0,0,0,0,0,1],
          [1,1,1,1,0,0,1,1,1,1,1,1]]

  def draw(self):
    #maze map

    for i in range (10):
      for j in range (12):
        if self.Maze[i][j]==1:
          pygame.draw.rect(screen, (255,0,0), (j*50,i*50,50,50))
        else:
          pygame.draw.rect(screen, (255,255,255), (j*50,i*50,50,50), 1)
        if self.Maze[i][j]==9:
          #start position for player
          pygame.draw.rect(screen, (255,255,255), (j*50,i*50,50,50))


  def collide (self,px, py, direction):

    if direction is RIGHT:
          #print("checking ", px, " , ",py, "and row/column", px/50, " , ",py/50)
      if self.Maze[int(py/50)][int((px+20)/50)]==1:
        print("collision from right!")
        return True
      else:
        print("no collision")
    if direction is LEFT:
      if self.Maze[int((py)/50)][int((px)/50)]==1:
        print("brrrrrrrrrrrrrrrrr")
        return True
      else:
        print("no left collision")
    if direction is DOWN:
      if self.Maze[int((py+20)/50)][int((px)/50)]==1:
        print("feet collision")
        return True
      else:
        print("no down collision")
    if direction is UP:
      if self.Maze[int((py)/50)][int((px)/50)]==1:
        print("aaaaaaaaaaaa")
        return True
      else:
        print("no up collision")

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
    if direction == UP or direction == DOWN:
      pVy *=-1

  xpos += pVx
  ypos += pVy

  #render section-----------------------------------------------
  screen.fill((0,0,0))

  m1.draw()
  player = pygame.draw.rect(screen, PINK, (xpos,ypos,pW,pH))


  pygame.display.flip()

pygame.quit()#end of loop
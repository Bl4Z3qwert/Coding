import pygame
import math
import random
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Shooter')



#images
player=pygame.image.load('player.png')
enemy=pygame.image.load('enemy.png')
bullet=pygame.image.load('bullet.png')
#player
player_x=370
player_y=500
player_move=0

#enemy
enemy_x=random.randint(0,700)
enemy_y=50
enemy_move_x=4
enemy_move_y=40

#bullet
bullet_x=0
bullet_y=player_y
bullet_move=10
bullet_state='ready'


def fire(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bullet,(x + 16 , y-10))
    
def is_collision(x1,y1,x2,y2):
    return math.hypot(x2-x1,y2-y1)<27 




run=True
while run:
   screen.fill((0,20,50))
   for event in pygame.event.get():
       if event.type==pygame.QUIT:
        run=False
        
       elif event.type==pygame.KEYDOWN:
           if event.key==pygame.K_LEFT:
               player_move=5    
           if event.key==pygame.K_RIGHT:
               player_move=5       
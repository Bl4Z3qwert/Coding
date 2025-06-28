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
               player_move=-5    
           if event.key==pygame.K_RIGHT:
               player_move=5   
           if     event.key==pygame.K_SPACE and bullet_state=='reday':
               bullet_x=player_x
               bullet_y=player_y
               fire(bullet_x,bullet_y)
       elif event.type==pygame.KEYUP:
           if event.key  in [pygame.K_LEFT,pygame.K_RIGHT] :
               player_move=0
   player_x+=player_move
   player_x=max(0,min(player_x,736))
   
   
   
   enemy_x+=enemy_move_x
   if enemy_x<=0 or enemy_x>=736:
       enemy_move_x*=-1
       enemy_y+=enemy_move_y
   if bullet_state=='fire':
       fire(bullet_x,bullet_y)
       bullet_y-=bullet_move
       if bullet_y <=0:
           bullet_state='ready'
           
   if bullet_state=='fire' and is_collision(enemy_x,enemy_move_y,bullet_x,bullet_y):
       bullet_state='ready'
       enemy_x=random.randint(0,736)  
       enemy_y=50
       
   screen.blit(player,(player_x,player_y))        
   screen.blit(enemy,(enemy_x,enemy_y))
   pygame.display.update()         
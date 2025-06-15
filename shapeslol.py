import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
WHITE=((255,255,255))
pygame.draw.circle(screen,WHITE,(300,300),50)
pygame.draw.circle(screen,WHITE,(200,200),50)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.QUIT()
pygame.flip()    

            
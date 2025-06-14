

import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
surface = pygame.Surface((300,300))
screen.blit(image=(300,300))
pygame.image.load('OIP.jfif')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My first game screen")
GRAY = (58, 58, 58)
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT()
    pygame.display.flip()
    
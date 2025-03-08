import pygame
import random
pygame.init()

WIDTH, HEIGHT = 600,400
screen =pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption('rock,paper,scissors')


WHITE= (255,255,255)
BLACK= (0,0,0)
rock= pygame.image.load('download.jfif')
paper= pygame.image.load('OIP.jfif')
scissors= pygame.image.load('OIP(1).jfif')

rock= pygame.transform.scale(rock(100,100))
paper=pygame.transform.scale(paper(100,100))
scissors=pygame.transform.scale(scissors(100,100))

player_choices = {
    'rock':
}
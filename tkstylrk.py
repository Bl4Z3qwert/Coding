import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Let's Level Up The Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = [RED, BLUE]

# Define custom event
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 300)
import pygame
import sys

# Initialize Pygame
pygame.init()

# Window settings
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

# Colors
WHITE = (255, 255, 255)
RECT_COLOR = (0, 128, 255)  # You can change this to any RGB color

# Font settings
font = pygame.font.Font(None, 36)
text = font.render("Welcome to my game!", True, (0, 0, 0))  # Black text
text_rect = text.get_rect(center=(screen_width // 2, 50))

# Rectangle settings
rect_width = 200
rect_height = 100
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, rect_width, rect_height))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()

import pygame
import sys

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set-up
WIDTH = 800
HEIGHT = 600
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mouse Drawing App")
screen.fill(WHITE)

# Variables
drawing = False
last_pos = None

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = pygame.mouse.get_pos()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = pygame.mouse.get_pos()
            if last_pos:
                pygame.draw.line(screen, BLACK, last_pos, current_pos, 2)
            last_pos = current_pos
    
    # Update the display
    pygame.display.update()


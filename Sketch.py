import pygame
import sys

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

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
is_eraser = False
current_color = BLACK
is_eraser = False

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        
    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center = self.rect.center)
        surface.blit(text, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

def toggle_eraser():
    global is_eraser, current_color
    is_eraser = not is_eraser
    current_color = WHITE if is_eraser else BLACK

eraser_Button = Button(10,10, 60, 30, "Eraser", toggle_eraser)
    
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
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
                pygame.draw.line(screen, current_color, last_pos, current_pos, 2)
            last_pos = current_pos
        
        eraser_Button.handle_event(event)

    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 50))
    eraser_Button.draw(screen)
    
    # Update the display
    pygame.display.update()


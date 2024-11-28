import pygame

#initialize pygame:
pygame.init()

#create a display surface and declare its caption:
WINDOW_WITH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WITH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello Pygame")

#The main game loop:
running = True

while running:
    # loop through list of event objects:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# End the game
pygame.quit()            
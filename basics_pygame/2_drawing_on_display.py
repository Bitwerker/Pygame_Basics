import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

# Define coplours as RGB Tuples

BLACK = (0,0,0,)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MARGENTA = (255,0,255)

# Give a Backgroundcolor to the display

display.fill(BLUE)

# draw various shapes on our display:

pygame.draw.line(display,RED,(0,0),(100,100),5)
pygame.draw.line(display,GREEN,(100,100),(200,300),1)
pygame.draw.circle(display,WHITE, (WINDOW_WIDTH//2,WINDOW_HEIGHT//2),200, 6)
pygame.draw.circle(display,YELLOW, (WINDOW_WIDTH //2 , WINDOW_HEIGHT //2),195,0 )
pygame.draw.rect(display,CYAN,(500,0,100,100))
pygame.draw.rect(display,MARGENTA,(500,100,100,100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

# Ende:

pygame.quit()            
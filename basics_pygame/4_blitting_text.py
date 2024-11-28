import pygame

pygame.init()

WIND_WIDTH = 600
WIND_HEIGHT = 300

display_surface = pygame.display.set_mode((WIND_WIDTH, WIND_HEIGHT))
pygame.display.set_caption("Blitting Text")

# define colors:

GREEN = (0,255,0)
DARKGREEN = (10,50,10)
BLACK = (0,0,0)

# see all available System fonts

fonts = pygame.font.get_fonts()

for font in fonts:
    print(font)

#Define Fonts

system_font = pygame.font.SysFont("robotocondensed",64)
custom_font = pygame.font.Font("AttackGraffiti.ttf", 32)

# Define Text:
 
system_text = system_font.render("Dragons rule !!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WIND_WIDTH//2, WIND_HEIGHT //2)

custom_text = custom_font.render("Move the dragon soon" , True, GREEN )
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WIND_WIDTH//2,WIND_HEIGHT//2 + 100 )
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.blit(system_text,system_text_rect)
    display_surface.blit(custom_text,custom_text_rect)
    pygame.display.update()

pygame.quit()
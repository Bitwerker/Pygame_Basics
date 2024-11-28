import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Image blitting")

# Create images -> returnes a surface object with the image dranw on it:
# then we can get the rect of this image , to position the image

dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_rigth_image = pygame.image.load("dragon_right.png")
dragon_rigth_rect = dragon_rigth_image.get_rect()
dragon_rigth_rect.topright = (WINDOW_WIDTH,0)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(dragon_left_image,dragon_left_rect)
    display_surface.blit(dragon_rigth_image,dragon_rigth_rect)

    pygame.draw.line(display_surface,(255,255,255),(0,75),(WINDOW_WIDTH,75),4)

    pygame.display.update()

pygame.quit()
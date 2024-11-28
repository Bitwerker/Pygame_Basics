import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard movement")

#set game values:

VELOCITY = 10

dragon_image_surface = pygame.image.load("dragon_right.png")
dragon_image_rect = dragon_image_surface.get_rect()
dragon_image_rect.centerx = WIDTH//2
dragon_image_rect.bottom = HEIGHT

running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_image_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_image_rect.x += 10     
            if event.key == pygame.K_UP:
                dragon_image_rect.y -= 10
            if event.key == pygame.K_DOWN:
                dragon_image_rect.y += 10        


    display_surface.fill((0,0,0))            
    # copy / blitting the image to the display surface:
    display_surface.blit(dragon_image_surface, dragon_image_rect)
    # update the display to see the changes  :-)
    pygame.display.update()

pygame.quit()

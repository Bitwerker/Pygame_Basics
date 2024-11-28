import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse movement")

running = True

# loading assets:

dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       # moving by clicking left mousebutton:

        #if event.type == pygame.MOUSEBUTTONDOWN:          
            #mouse_x = event.pos[0]
            #print ("Mouse_x: " + str(mouse_x))
            #mouse_y = event.pos[1]
            #print ("Mouse_y: " + str(mouse_y))
            #dragon_rect.centerx = mouse_x
            #dragon_rect.centery = mouse_y
        # moving by mouse motion and also mouse button left is down:    
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1 :            
            print(event)    
            mouse_x = event.pos[0]
            print ("Mouse_x: " + str(mouse_x))
            mouse_y = event.pos[1]
            print ("Mouse_y: " + str(mouse_y))
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)

    pygame.display.update()        


pygame.quit()
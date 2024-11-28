import pygame

pygame.init()

WIN_WIDTH = 600
WIN_HEIGTH = 400

display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))
pygame.display.set_caption("Adding some Sound")

# load sounds: 

sound_1 = pygame.mixer.Sound("sound_1.wav")
sound_2 = pygame.mixer.Sound("sound_2.wav")

#load backgroundmusic:

pygame.mixer.music.load("music.wav")



# play sound effects:

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)
sound_2.set_volume(.1)
pygame.time.delay(2000)
#play and stop the music:

pygame.mixer.music.play(-1,0.0)

pygame.time.delay(5000)
# stop the background music:

pygame.mixer.music.stop()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
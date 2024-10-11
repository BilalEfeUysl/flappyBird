import pygame

pygame.init()

# these will determine the size of the screen
width = 500
height = 750

# defining the main settings of the game
screen = pygame.display.set_mode(width,height)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()


flag = True
while flag:

    # to exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # for updating the screen
    pygame.display.update()   
    
    # fps
    clock.tick(144)



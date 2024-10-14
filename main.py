import pygame

pygame.init()

# these will determine the size of the screen
width = 400
height = 600

# defining the main settings of the game
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# load background
background = pygame.image.load("background.jpg")


flag = True
while flag:
    
    # add background
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False    # to exit the game
    
    # for updating the screen
    pygame.display.update()   
    
    # fps
    clock.tick(144)

#quit the program
pygame.quit()


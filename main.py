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

# load bird
birdImage = pygame.image.load("bird.jpg")

# coordinate bird
bird_x = 45
bird_y = 250
bird_y_change = 0

flag = True
while flag:

    # add background to screen
    screen.blit(background,(0,0))

    
    for event in pygame.event.get():
        # to exit the game
        if event.type == pygame.QUIT:
            flag = False    
        # when the button pressed 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -4
        # when the button is not pressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 2

    # update coordinate 
    bird_y += bird_y_change

    # limiting the bird's range
    if bird_y <= 0:
        bird_y = 0
    elif bird_y >= 500:
        bird_y = 500    

    # add bird to screen
    screen.blit(birdImage,(bird_x,bird_y))


    # for updating the screen
    pygame.display.update()   
    
    # fps
    clock.tick(144)

#quit the program
pygame.quit()


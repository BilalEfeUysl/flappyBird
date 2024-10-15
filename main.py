import pygame
import random 

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

pipe_width = 70
pipe_height = random.randint(150,250)
pipe_color = (0,255,0)
pipe_x = 400
pipe_x_change = -4

def display_pipe(height):
    pygame.draw.rect(screen,pipe_color,(pipe_x,0,pipe_width,height))

    bottom_pipe_y = height+150

    pygame.draw.rect(screen,pipe_color,(pipe_x,bottom_pipe_y,pipe_width,(550-bottom_pipe_y)))


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

    pipe_x += pipe_x_change
    if pipe_x<= -10:
        pipe_x = 400
        pipe_height = random.randint(150,300)
    display_pipe(pipe_height)        

    # add bird to screen
    screen.blit(birdImage,(bird_x,bird_y))


    # for updating the screen
    pygame.display.update()   
    
    # fps
    clock.tick(144)

#quit the program
pygame.quit()


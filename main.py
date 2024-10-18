import pygame
import random 

pygame.init()


# these will determine the size of the screen
width = 400
height = 600

# Score 
score = 0
scoreFont = pygame.font.Font(None,36)
def score_display(score):
    display = scoreFont.render(f"Score: {score}",True,(255,255,255))
    screen.blit(display,(10,10))

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

# pipe view
pipe_width = 70
pipe_height = random.randint(150,250)
pipe_color = (0,255,0)
pipe_x = 400
pipe_x_change = -1  

# function of creating pipe
def display_pipe(height):
    pygame.draw.rect(screen,pipe_color,(pipe_x,0,pipe_width,height))

    bottom_pipe_y = height+150

    pygame.draw.rect(screen,pipe_color,(pipe_x,bottom_pipe_y,pipe_width,(550-bottom_pipe_y)))

# while loop to wait on start screen    
wait = True
while wait:
    # add background to screen 
    screen.blit(background,(0,0))

    font = pygame.font.Font(None, 45)

    welcome_text = font.render("PRESS THE SPACE", True, (0,0,0))

    screen.blit(welcome_text,(70,70))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                wait = False
        if event.type == pygame.QUIT:
            wait = False    

    pygame.display.update()

game_over = True
flag = True
while flag:

    # add background to screen
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        # to exit the game
        if event.type == pygame.QUIT:
            flag = False
            game_over = False
        # when the button pressed 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -3
        # when the button is not pressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 1

    # update coordinate 
    bird_y += bird_y_change

    # limiting the bird's range
    if bird_y <= 0:
        bird_y = 0
    elif bird_y >= 500:
        bird_y = 500    

    # repeat of the pipe
    pipe_x += pipe_x_change
    if pipe_x<= -10:
        pipe_x = 400
        pipe_height = random.randint(150,300)
        score += 1
    display_pipe(pipe_height)        

    # control of bird touching pipes
    if pipe_x <= 110:
        if bird_y <= pipe_height or bird_y >= pipe_height + 101:
            flag = False        

    # add bird to screen
    screen.blit(birdImage,(bird_x,bird_y))

    # writing the score on the screen
    score_display(score)   

    # for updating the screen
    pygame.display.update()   
    
    # fps
    clock.tick(144)

# creating the game over text
wait = True
while wait:

    font = pygame.font.Font(None, 60)

    game_over_text = font.render("GAME OVER", True, (255, 105, 180))

    screen.blit(game_over_text,(75,250))

    # to exit the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                wait = False
        if event.type == pygame.QUIT:
            wait = False    

    pygame.display.update()


#quit the program
pygame.quit()


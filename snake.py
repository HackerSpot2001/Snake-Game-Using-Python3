# Adding sound and background image  in snake game

import pygame
import random

pygame.mixer.init()
pygame.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)
# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background image 
# bgimg = pygame.image.load("bg1.jpg")
# bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()


def music(path):
    pygame.mixer_music.load(path)
    pygame.mixer_music.play()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while exit_game!= True:
        gameWindow.fill((33,3,6))
        text_screen("Welcome To Snake Game ",white,250,250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # music("bg.mp3")
                    game_loop()
        pygame.display.update()
        clock.tick(40)
# Game Loop
def game_loop():

    # Game Title
    pygame.display.set_caption("Snake Game")
    pygame.display.update()

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 3
    snake_size = 20
    fps = 60
    snk_list = []
    snk_length = 1
    while not exit_game:
        if game_over:
            gameWindow.fill((23,34,45))
            text_screen(f"Game Over! your score is {score*10} and Press Enter To Continue",red,130,250)
            # music("Alien_Beam.mp3")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # music("bg.mp3")
                        game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

            gameWindow.fill((233,89,77))
            # gameWindow.blit(bgimg,(0,0))
            
            text_screen("Score: " + str(score), white, 5, 5)
            pygame.draw.rect(gameWindow,(255,255,255), [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
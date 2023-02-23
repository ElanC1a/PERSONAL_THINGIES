#create a snake game using pygame 
import pygame
import sys
import random
import time

#initialize pygame
pygame.init()

#set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

#set up the colors
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

#fps controller
fps_controller = pygame.time.Clock()

#game variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

#game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Game Over!', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width/2, window_height/4)
    window.blit(game_over_surface, game_over_rect)
    show_score(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

#show score function
def show_score(choice=1):
    s_font = pygame.font.SysFont('times new roman', 20)
    s_surface = s_font.render('Score : {0}'.format(score), True, black)
    s_rect = s_surface.get_rect()
    if choice == 1:
        s_rect.midtop = (80, 10)
    else:
        s_rect.midtop = (window_width/2, window_height/1.25)
    window.blit(s_surface, s_rect)

#main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #validation of direction
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    #update snake position [x, y]
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    #snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    #food spawn
    if food_spawn == False:
        food_position = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
    food_spawn = True

    #background
    window.fill(white)

    #draw snake
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    #draw food
    pygame.draw.rect(window, brown, pygame.Rect(food_position[0], food_position[1], 10, 10))

    #bound
    if snake_position[0] > window_width-10 or snake_position[0] < 0:
        game_over()
    if snake_position[1] > window_height-10 or snake_position[1] < 0:
        game_over()
    
    #self hit
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    #common stuff
    show_score()
    pygame.display.flip()
    fps_controller.tick(20)
    

if __name__ == '__main__':
    main()
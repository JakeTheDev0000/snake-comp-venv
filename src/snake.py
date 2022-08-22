# username = "Jakeplays0000"

import pygame, sys, time, random
import emailSend, launcher, configMgr
from PySimpleGUI import popup as popup
 
def snakePlay(loop=False, practice=False):
    # Difficulty settings
    # Easy      ->  10
    # Medium    ->  25
    # Hard      ->  40
    # Harder    ->  60
    # Impossible->  120
    difficulty = int(configMgr.getDifficulty())
    speed_snake = int(configMgr.getSpeedSnake())

    # Window size
    frame_size_x = int(configMgr.get_frame_size_x())
    frame_size_y = int(configMgr.get_frame_size_y())
    # in case of fullscreen

    print("frame_size_x: " + str(frame_size_x))
    print("frame_size_y: " + str(frame_size_y))


    #fullscreen

    # Checks for errors encountered
    print("initializing pygame")
    check_errors = pygame.init()
    print("pygame initialized")
    # pygame.init() example output -> (6, 0)
    # second number in tuple gives number of errors
    print("checking for errors")
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialised')
    
    print("setting up game window")


    # Initialise game window
    pygame.display.set_caption('Snake Eater')
    if configMgr.getFullscreen() == "True":
        game_window = pygame.display.set_mode((frame_size_x, frame_size_y), pygame.FULLSCREEN)
    elif configMgr.getFullscreen() == "False":
        game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    else:
        print("fullscreen config error")
        popup("fullscreen config error")
        launcher.main()

    # game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    # game_window = pygame.display.set_mode((frame_size_x, frame_size_y), pygame.FULLSCREEN)

    print("setting up game window complete")
    print("hideing mouse")
    pygame.mouse.set_visible(False)
    print("mouse hidden")


    print("setting up colors")
    # Colors (R, G, B)
    black = pygame.Color(0, 112, 30)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(245, 100, 22)
    blue = pygame.Color(0, 0, 255)
    print("colors set up")

    # FPS (frames per second) controller
    fps_controller = pygame.time.Clock()



    # Game variables
    print("setting up game variables")
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction

    score = 0
    print("game variables set up")

    # Game Over
    print("setting up game over")
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render(configMgr.getUsername() + " killed " + configMgr.getSnakeName(), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)    

        game_window.fill(pygame.Color(0, 0, 0))
        game_window.blit(game_over_surface, game_over_rect)


        if practice == False:
            emailSend.sendEmail(score, True, difficulty, speed_snake, snake_pos, food_pos, food_spawn, direction, change_to)
        else:
            pass
        pygame.display.flip()
        print("Your score was: ", score)
        show_score(0, red, 'times', 20)
        time.sleep(2)
        if loop == True:
            snakePlay()
        else:        
            pygame.quit()
            launcher.main()
    print("game over set up")

    # Score
    print("setting up score")
    def show_score(choice, color, font, size):
        pygame.font.init()
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x/10, 15)
        else:
            score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
        
        try:
            game_window.blit(score_surface, score_rect)
        except Exception as e:
            print(e)
        # pygame.display.flip()
    print("score set up")


    print("setting up main game loop")
    def show_vars(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Difficulty: ' + str(difficulty) + ' Speed: ' + str(speed_snake) + ' pos1: ' + str(snake_pos[0]) + ' pos2: ' + str(snake_pos[1]) + ' Fps: ' + str(int(fps_controller.get_fps())), True, color)
        score_rect = score_surface.get_rect()
        if choice == 10:
            score_rect.midtop = (frame_size_x/10, 15)
        else:
            score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
        try:
            game_window.blit(score_surface, score_rect)
        except Exception as e:
            print(e)
        # pygame.display.flip()

    # Main logic
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Whenever a key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # W -> Up; S -> Down; A -> Left; D -> Right
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        change_to = 'RIGHT'
                    # Esc -> Create event to quit the game
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            # Making sure the snake cannot move in the opposite direction instantaneously
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'

            # Moving the snake
            if direction == 'UP':
                snake_pos[1] -= speed_snake
            if direction == 'DOWN':
                snake_pos[1] += speed_snake
            if direction == 'LEFT':
                snake_pos[0] -= speed_snake
            if direction == 'RIGHT':
                snake_pos[0] += speed_snake

            # Snake body growing mechanism
            snake_body.insert(0, list(snake_pos))
            if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
                score += 1
                food_spawn = False
            else:
                snake_body.pop()

            # Spawning food on the screen
            if not food_spawn:
                food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
            food_spawn = True

            # GFX
            game_window.fill(black)
            for pos in snake_body:
                # Snake body
                # .draw.rect(play_surface, color, xy-coordinate)
                # xy-coordinate -> .Rect(x, y, size_x, size_y)
                pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

            # Snake food
            pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

            # Game Over conditions
            # Getting out of bounds
            if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
                print("reason of game over: out of bounds -- 1")
                print("vars: snake_pos[0] = ", snake_pos[0], "frame_size_x = ", frame_size_x)
                print("snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10")
                game_over()
            if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
                print("reason of game over: out of bounds -- 2")
                print("vars: snake_pos[1] = ", snake_pos[1], "frame_size_y = ", frame_size_y)
                print("snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10")
                game_over()
            # Touching the snake body
            for block in snake_body[1:]:
                if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                    print("reason of game over: touching the snake body")
                    game_over()

            show_score(1, white, 'consolas', 20)
            show_vars(1, white, 'consolas', 20)
            # Refresh game screen
            try:
                pygame.display.update() 
            except Exception as e:
                    print(e)
            # Refresh rate
            fps_controller.tick(difficulty)
    except Exception as e:
        print(e)
        

def ranByUser():
    print("run \"launcher\"")
    sys.exit(-1)

if __name__ == "__main__":
    ranByUser()
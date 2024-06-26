import pygame
from striker import Striker
from ball import Ball

WIDTH = 800
HEIGHT = 400

# initializing stuff
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

game_font = pygame.font.Font(None, 50)

def runGame():
    # now making strikers and ball
    left_striker = Striker(10, 200, 15, 60, (0, 0, 255), screen)
    right_striker = Striker(775, 200, 15, 60, (255, 0, 0), screen)
    ball = Ball(400, 200, 10, 3, 3, (255, 255, 255), screen)

    
    running = True
    winner = ""
    text = pygame.Surface((1, 1))
    while running:
        # black screen
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        # handling user input for keys on both the players!
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            left_striker.move('up')
        if keys[pygame.K_d]:
            left_striker.move('down')
        if keys[pygame.K_LEFT]:
            right_striker.move('down')
        if keys[pygame.K_RIGHT]:
            right_striker.move('up')


        ball.move()
        ball.check_collision(left_striker)
        ball.check_collision(right_striker)

        gameover = ball.collision_with_wall()
        if gameover == 'left':
            winner = "RED"
            running = False
        elif gameover == 'right':
            winner = "BLUE"
            running = False

        left_striker.display()
        right_striker.display()
        ball.display()
        pygame.display.update()
        clock.tick(60)

    if winner:
        screen.fill((0, 0, 0))
        if winner == "RED":
            text = game_font.render("RED WINS!", False, (255, 0, 0))
            screen.blit(text, (290, 180))

        elif winner == "BLUE":
            text = game_font.render("BLUE WINS!", False, (0, 0, 255))
            screen.blit(text, (280, 180))

        pygame.display.update()
        pygame.time.wait(2000)


while True:
    runGame()
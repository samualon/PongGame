import pygame, sys, random
from pygame import mixer

# Ball Animation
def ball_animation():
    global ball_speed_y, ball_speed_x
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_widght:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):

        ball_speed_x *= -1

# Player Animation
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

# Opponent AI
def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# Ball restart
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_widght/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# General setup
pygame.init()
clock = pygame.time.Clock()
screen_widght = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_widght, screen_height))
pygame.display.set_caption("Pong")

# Game rectanles
ball = pygame.Rect(screen_widght/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_widght - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#Background color and rectangle colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

#General speeds
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

#Sounds used
#ball_sound = mixer.Sound("")

# Main loop
while True:
    # Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)

    # Updating window
    pygame.display.flip()
    clock.tick(75)

import pgzrun, os, pygame, random
import time

loaded = False

WIDTH = 1100
HEIGHT = 900
TITLE = "SNAKE"
os.environ["SDL_VIDEO_WINDOW_POS"] = "center"

speed = 5

current_frame = 0
frame_count = 0
frame_interval = 10

apple = pygame.image.load('images/apple.png')
scaled_apple = pygame.transform.scale(apple, (80, 80))
pygame.image.save(scaled_apple, 'images/apple.png')

snake_head = pygame.image.load('images/snake head.png')
scaled_snake_head = pygame.transform.scale(snake_head, (80, 80))
pygame.image.save(scaled_snake_head, 'images/snake head.png')

snake_body = pygame.image.load('images/snake body.png')
scaled_snake_body = pygame.transform.scale(snake_body, (80, 80))
pygame.image.save(scaled_snake_body, 'images/snake body.png')

apple = Actor("apple")
apple.pos = (random.randint(50, 500), random.randint(50, 500))

snake_head = Actor("snake head")
snake_head.pos = WIDTH / 2, HEIGHT / 2 + 300

snake_body = Actor("snake body")

def draw():
    global loaded
    screen.blit("background", (0, 0))
    apple.draw()
    snake_head.draw()
    snake_body.draw()
    loaded = True

def add_body():
    pass

def update():
    global frame_count, current_frame, pipe_timer
    frame_count += 1
    if keyboard.w:
        if snake_head.angle != 0:
            snake_head.angle = 180

    if keyboard.a:
        if snake_head.angle != 90:
            snake_head.angle = -90

    if keyboard.s:
        if snake_head.angle != 180:
            snake_head.angle = 0

    if keyboard.d:
        if snake_head.angle != -90:
            snake_head.angle = 90

    if loaded:
        if snake_head.angle == 180:
            snake_head.y -= speed

        if snake_head.angle == -90:
            snake_head.x -= speed

        if snake_head.angle == 0:
            snake_head.y += speed

        if snake_head.angle == 90:
            snake_head.x += speed

pgzrun.go()
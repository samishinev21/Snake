import pgzrun, os, pygame, random

WIDTH = 1100
HEIGHT = 900
TITLE = "SNAKE"
os.environ["SDL_VIDEO_WINDOW_POS"] = "center"

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
    screen.blit("background", (0, 0))
    apple.draw()
    snake_head.draw()
    snake_body.draw()

def add_body():
    pass

def update():
    pass

pgzrun.go()
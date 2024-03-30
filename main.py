import pygame 
import random
import time

clock = pygame.time.Clock()
class Window:
    WSIZE = (720, 380)
    screen = pygame.display.set_mode(WSIZE)

    TSIDE = 30
    MSIZE = WSIZE[0] // TSIDE, WSIZE[1] // TSIDE

    pygame.font.init()
    font_score = pygame.font.SysFont("Arial", 20)
    font_gameover = pygame.font.SysFont("Arial", 40)
    font_space = pygame.font.SysFont("Arial", 15)

    start_pos = MSIZE[0] // 2, MSIZE[1] // 2

snake = [Window.start_pos]
alive = True
direction = 0
directions = [(1,0), (0,1), (-1,0), (0,-1)]

apple =  random.randint(0, Window.MSIZE[0]), random.randint(0, Window.MSIZE[1])

fps = 5

running = True
while running:
    clock.tick(fps)
    Window.screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if alive:
                if event.key == pygame.K_RIGHT and direction != 2:
                    direction = 0
                elif event.key == pygame.K_DOWN and direction != 3:
                    direction = 1
                elif event.key == pygame.K_LEFT and direction != 0:
                    direction = 2
                elif event.key == pygame.K_UP and direction != 1:
                    direction = 3
            else:
                if event.key == pygame.K_SPACE:
                    alive = True
                    snake = [Window.start_pos]
                    apple =  random.randint(0, Window.MSIZE[0]), random.randint(0, Window.MSIZE[1])

    [pygame.draw.rect(Window.screen, "green", (x * Window.TSIDE, y * Window.TSIDE, Window.TSIDE - 1, Window.TSIDE - 1)) for x, y in snake]
    pygame.draw.rect(Window.screen, "red", (apple[0] * Window.TSIDE, apple[1] * Window.TSIDE, Window.TSIDE - 1, Window.TSIDE - 1))

    if alive:
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        if not(0 <= new_pos[0] < Window.MSIZE[0] and 0 <= new_pos[1] < Window.MSIZE[1]) or \
                new_pos in snake:
            alive = False
        else:
            snake.insert(0, new_pos)
            if new_pos == apple:
                fps += 1
                apple = random.randint(0, Window.MSIZE[0]), random.randint(0, Window.MSIZE[1])
            else:
                snake.pop(-1)
    else:
        text = Window.font_gameover.render(f"Game Over", True, "White")
        Window.screen.blit(text, (Window.WSIZE[0] // 2 - text.get_width()//2, Window.WSIZE[1] // 2 - 50))
        text = Window.font_space.render(f"Press Space for restart", True, "White")
        Window.screen.blit(text, (Window.WSIZE[0] // 2 - text.get_width()//2, Window.WSIZE[1] // 2 - 50))
    Window.screen.blit(Window.font_score.render(f"Score: {len(snake)}", True, "yellow"), (5,5))

    pygame.display.flip()

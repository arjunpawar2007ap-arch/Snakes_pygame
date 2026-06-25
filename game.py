import pygame
import sys
import random

cell_size = 30
grid_width = 20
grid_height = 20

window_width = cell_size*grid_width
window_height = cell_size*grid_height

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

snake = [(10,10), (9,10), (8,10)]
direction = (1,0)
score = 0

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def spawn_food():
    while True:
        pos = (random.randint(0, grid_width-1), random.randint(0, grid_height-1))
        if pos not in snake:
            return pos

food = spawn_food()

def game_over():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 60)
    text = font.render(f'Game Over! Score: {score}', True, WHITE)
    rect = text.get_rect(center=(window_width//2, window_height//2))
    screen.blit(text, rect)
    
    font2 = pygame.font.SysFont(None, 30)
    text2 = font2.render('Press Q to quit or R to restart', True, WHITE)
    rect2 = text2.get_rect(center=(window_width//2, window_height//2 + 50))
    screen.blit(text2, rect2)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

while True:
    clock.tick(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != (0, 1):
                direction = (0, -1)
            if event.key == pygame.K_s and direction != (0, -1):
                direction = (0, 1)
            if event.key == pygame.K_a and direction != (1, 0):
                direction = (-1, 0)
            if event.key == pygame.K_d and direction != (-1, 0):
                direction = (1, 0)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = spawn_food()
    else:
        snake.pop()

    if (new_head[0] < 0 or new_head[0] >= grid_width or
    new_head[1] < 0 or new_head[1] >= grid_height or
    new_head in snake[1:]):
        game_over()
    
    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0]*cell_size, segment[1]*cell_size, cell_size-2, cell_size-2))

    pygame.draw.rect(screen, RED, (food[0]*cell_size, food[1]*cell_size, cell_size-2, cell_size-2))

    pygame.display.flip()
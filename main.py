import sys

import numpy as np
import pygame

BOARD_SIZE = 18
N_COLORS = 6
CELL_SIZE = 50
BACKGROUND_COLOR = (194, 173, 138)

colors = np.random.randint(255, size=(N_COLORS, 3))
board = np.random.randint(N_COLORS, size=(BOARD_SIZE, BOARD_SIZE))
window_size = CELL_SIZE * BOARD_SIZE
pygame.init()
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Flood-it!')

print(board[0])


def calculate_rects():
    rect_list = []
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect_i = (((1 + x) * CELL_SIZE) - CELL_SIZE,
                      ((1 + y) * CELL_SIZE) - CELL_SIZE,
                      CELL_SIZE, CELL_SIZE)
            rect_list.append(rect_i)
    return rect_list


def draw_board():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            pygame.draw.rect(surface=screen,
                             rect=(((1 + x) * CELL_SIZE) - CELL_SIZE,
                                   ((1 + y) * CELL_SIZE) - CELL_SIZE,
                                   CELL_SIZE, CELL_SIZE),
                             color=colors[board[x][y]])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            print(event.pos)
    screen.fill(BACKGROUND_COLOR)
    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()

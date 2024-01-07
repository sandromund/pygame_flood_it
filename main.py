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


def calculate_rects():
    rect_array = []
    for x in range(BOARD_SIZE):
        x_list = []
        for y in range(BOARD_SIZE):
            rect_i = (((1 + x) * CELL_SIZE) - CELL_SIZE,
                      ((1 + y) * CELL_SIZE) - CELL_SIZE,
                      CELL_SIZE, CELL_SIZE)
            x_list.append(rect_i)
        rect_array.append(x_list)
    return rect_array


rects = calculate_rects()


def draw_board():
    for x_board in range(BOARD_SIZE):
        for y_board in range(BOARD_SIZE):
            pygame.draw.rect(surface=screen,
                             rect=rects[x_board][y_board],
                             color=colors[board[x_board][y_board]])


def get_color_of_clicked_rect(mouse_position):
    """

    transformation math of calculate_rects()
    x_mouse ==  (1 + x) * CELL_SIZE) - CELL_SIZE
    x_mouse + CELL_SIZE == (1 + x) * CELL_SIZE
    ((x_mouse + CELL_SIZE) / CELL_SIZE) - 1 ==  x

    :param mouse_position:
    :return:
    """
    x_mouse, y_mouse = mouse_position
    x_new = ((x_mouse + CELL_SIZE) // CELL_SIZE) - 1
    y_new = ((y_mouse + CELL_SIZE) // CELL_SIZE) - 1
    return x_new, y_new


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            x, y = get_color_of_clicked_rect(event.pos)
            print(x, y)
    screen.fill(BACKGROUND_COLOR)
    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()

import sys

import numpy as np
import pygame

BOARD_SIZE = 14
N_COLORS = 6
CELL_SIZE = 50
N_MAX_MOVES = 25

colors = np.random.randint(255, size=(N_COLORS, 3))
board = np.random.randint(N_COLORS, size=(BOARD_SIZE, BOARD_SIZE))
connected = np.zeros(shape=(BOARD_SIZE, BOARD_SIZE))
connected[0][0] = 1
window_size = CELL_SIZE * BOARD_SIZE
pygame.init()
screen = pygame.display.set_mode((window_size, window_size))
moves_counter = 0


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
    return board[x_new][y_new]


def find_connection():
    queue = [(0, 0)]
    seen = set()
    while len(queue) > 0:
        x_i, y_j = queue.pop(0)
        if (x_i, y_j) in seen:
            continue
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_t = x_i + i
            y_t = y_j + j
            if 0 <= x_t < BOARD_SIZE and 0 <= y_t < BOARD_SIZE:
                if board[x_t][y_t] == board[0][0]:
                    connected[x_t][y_t] = 1
                    queue.append((x_t, y_t))
        seen.add((x_i, y_j))


def color_connected(new_color):
    if new_color == board[0][0]:
        return
    for x_board in range(BOARD_SIZE):
        for y_board in range(BOARD_SIZE):
            if connected[x_board][y_board] > 0:
                board[x_board][y_board] = new_color


find_connection()

running = True
while running:
    pygame.display.set_caption(f'Flood-it! - Move: {moves_counter} / {N_MAX_MOVES}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            clicked_color = get_color_of_clicked_rect(mouse_pos)
            color_connected(clicked_color)
            find_connection()
            moves_counter += 1
    draw_board()

    pygame.display.flip()

pygame.quit()
sys.exit()

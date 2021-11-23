import random
try:
    import numpy as np
except:
    print("Please install numpy module")

try:
    import pygame
except:
    print("Please import pygame module")
from pygame.math import Vector2
import time


class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.bg_color = (28, 170, 156)
        self.line_color = (23, 145, 135)
        self.board = np.zeros((3, 3))
        self.block_size = (800 // 3)
        self.player = 1
        self.space = 55
        self.block_width = 20
        self.circle_width = 15
        self.radius = 65
        self.mouse_pos = None
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.running = True

    def draw_x_or_o(self, y, x, player):
        self.board[y][x] = player

    def empty_block(self, y, x):
        return self.board[y][x] == 0

    def draw_lines(self):
        for i in range(1, 3):
            pygame.draw.line(self.surface, self.line_color, (i * self.width // 3, 0), (i * self.width // 3, 800), 15)
        for i in range(1, 3):
            pygame.draw.line(self.surface, self.line_color, (0, i * self.height // 3), (800, i * self.height // 3), 15)

    def draw_blocks(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    pygame.draw.circle(self.surface, (0, 0, 0), (int(x * self.block_size + self.block_size / 2), int(y * self.block_size + self.block_size / 2)), self.radius, self.circle_width)
                if self.board[y][x] == 2:
                    pygame.draw.line(self.surface, (0, 255, 0), (x * self.block_size + self.space, y * self.block_size + self.block_size - self.space),
                                                            (x * self.block_size + self.block_size - self.space, y * self.block_size + self.space), self.block_width)
                    pygame.draw.line(self.surface, (0, 255, 0), (x * self.block_size + self.space, y * self.block_size + self.space),
                                                            (x * self.block_size + self.block_size - self.space, y * self.block_size + self.block_size - self.space), self.block_width)


    def update_board(self):
        if self.empty_block(self.mouse_pos[1], self.mouse_pos[0]):
            if self.player == 1:
                self.draw_x_or_o(self.mouse_pos[1], self.mouse_pos[0], self.player)
                self.player = 2
            elif self.player == 2:
                self.draw_x_or_o(self.mouse_pos[1], self.mouse_pos[0], self.player)
                self.player = 1


    def win(self):
        for y in range(3):
            if self.board[y][0] == 1 and self.board[y][1] == 1 and self.board[y][2] == 1:
                 self.draw_horizonal_line(y)
            if self.board[y][0] == 2 and self.board[y][1] == 2 and self.board[y][2] == 2:
                 self.draw_horizonal_line(y)
        for x in range(3):
            if self.board[0][x] == 1 and self.board[1][x] == 1 and self.board[2][x] == 1:
                 self.draw_vertical_line(x)
            if self.board[0][x] == 2 and self.board[1][x] == 2 and self.board[2][x] == 2:
                 self.draw_vertical_line(x)
        if self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1:
            self.draw_diagonal_line()
        if self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1:
            self.draw_revers_diagonal_line()
        if self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2:
            self.draw_diagonal_line()
        if self.board[0][2] == 2 and self.board[1][1] == 2 and self.board[2][0] == 2:
            self.draw_revers_diagonal_line()

    def draw_vertical_line(self, i):
        pygame.draw.line(self.surface, self.line_color, (i * self.width // 3 + self.block_size / 2, 0), (i * self.width // 3 + self.block_size / 2, 800), 8)

    def draw_horizonal_line(self, i):
        pygame.draw.line(self.surface, self.line_color, (0, i * self.height // 3 + self.block_size / 2), (800, i * self.height // 3 + self.block_size / 2), 8)

    def draw_diagonal_line(self):
        pygame.draw.line(self.surface, self.line_color, (0, 0), (800, 800), 8)

    def draw_revers_diagonal_line(self):
        pygame.draw.line(self.surface, self.line_color, (0, 800), (800, 0), 8)


    def play(self):
        self.surface.fill(self.bg_color)
        self.draw_lines()
        self.draw_blocks()
        self.win()

    def run(self):
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pos = (int(event.pos[0] / (800 // 3)), int(event.pos[1] / (800 // 3)))
                    self.update_board()
            
            self.play()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()

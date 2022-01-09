try:
    import pygame
except:
    print("Please import pygame module")
from pygame.math import Vector2
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sea Battle")
        self.bg_color = (255, 255, 255)
        self.line_color = (0, 0, 0)
        self.text_color = (0, 0, 0)
        self.block_size = 50
        self.left_margin = 200
        self.top_margin = 30
        self.height = self.top_margin + 15 * self.block_size
        self.width = self.left_margin + 30 * self.block_size
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('comicsans', int(self.block_size // 1.5))
        self.rungame = True

    def play(self):
        self.surface.fill(self.bg_color)
        self.draw_board()

    def draw_board(self):
        let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for y in range(11):
            for x in range(11):
                pygame.draw.line(self.surface, self.line_color, (self.left_margin, self.top_margin + y * self.block_size),
                        (self.left_margin + 10 * self.block_size, self.top_margin + y * self.block_size), 1)
                pygame.draw.line(self.surface, self.line_color, (self.left_margin + x * self.block_size, self.top_margin),
                        (self.left_margin + x * self.block_size, self.top_margin + 10 * self.block_size), 1)
                pygame.draw.line(self.surface, self.line_color, (self.left_margin + 15 * self.block_size, self.top_margin + y * self.block_size),
                        (self.left_margin + 10 * self.block_size + 15 * self.block_size, self.top_margin + y * self.block_size), 1)
                pygame.draw.line(self.surface, self.line_color, (self.left_margin + x * self.block_size + 15 * self.block_size, self.top_margin),
                        (self.left_margin + x * self.block_size + 15 * self.block_size, self.top_margin + 10 * self.block_size), 1)
            
            if y < 10:
                num = self.font.render(str(y + 1), 1, self.text_color)
                letters = self.font.render(let[y], 1, self.text_color)

                w_num = num.get_width()
                h_num = num.get_height()
                w_let = letters.get_width()

                self.surface.blit(num, (self.left_margin - (w_num // 2 + self.block_size // 2),
                    self.top_margin + y * self.block_size + (self.block_size // 2 - h_num // 2)))
                self.surface.blit(letters, (self.left_margin + y * self.block_size + (self.block_size // 2 - w_let // 2),
                    self.top_margin + 10 * self.block_size + self.block_size // 4))
                self.surface.blit(num, (self.left_margin - (w_num // 2 + self.block_size // 2) + 15 * self.block_size,
                    self.top_margin + y * self.block_size + (self.block_size // 2 - h_num // 2)))
                self.surface.blit(letters, (self.left_margin + y * self.block_size + (self.block_size // 2 - w_let // 2) + 15 * self.block_size,
                    self.top_margin + 10 * self.block_size + self.block_size // 4))


    def run(self):
        while self.rungame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rungame = False

            self.play()
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()

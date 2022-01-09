try:
    import pygame
except:
    print("Please import pygame module")
from pygame.math import Vector2
import random

class Block:
    def __init__(self, surface, width, height, cols, rows, blue, green, red, bg):
        self.surface = surface
        self.swidth = width
        self.sheight = height
        self.cols = cols
        self.rows = rows
        self.blue = blue
        self.green = green
        self.red = red
        self.bg = bg
        self.width = self.swidth // cols
        self.height = 50
        self.blocks = None

    def create_block(self):
        self.blocks = []
        block_ind = []
        for row in range(self.rows):
            blocks_row = []
            for col in range(self.cols):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                else:
                    strength = 1
                block_ind = [rect, strength]
                blocks_row.append(block_ind)
            self.blocks.append(blocks_row)

    def draw_block(self):
        for row in self.blocks:
            for block in row:
                if block[1] == 3:
                    color = self.blue
                if block[1] == 2:
                    color = self.green
                if block[1] == 1:
                    color = self.red
                pygame.draw.rect(self.surface, color, block[0])
                pygame.draw.rect(self.surface, self.bg, block[0], 2)

class Line:
    def __init__(self, surface, width, height, cols, rows, blue, green, red, bg):
        self.surface = surface
        self.swidth = width
        self.sheight = height
        self.cols = cols
        self.rows = rows
        self.blue = blue
        self.green = green
        self.red = red
        self.bg = bg
        self.height = 20
        self.line_col = (142, 135, 123)
        self.outline_col = (100, 100, 100)
        self.width = int(self.swidth // self.cols)
        self.x = int((self.swidth // 2) - self.width // 2)
        self.y = self.sheight - (self.height * 2)
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
        self.move_true = True

    def move(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0 and self.move_true:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < self.swidth and self.move_true:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(self.surface, self.line_col, self.rect)
        pygame.draw.rect(self.surface, self.outline_col, self.rect, 3)

    def reset(self):
        self.height = 20
        self.line_col = (142, 135, 123)
        self.outline_col = (100, 100, 100)
        self.width = int(self.swidth // self.cols)
        self.x = int((self.swidth // 2) - self.width // 2)
        self.y = self.sheight - (self.height * 2)
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
        self.move_true = True

class Ball:
    def __init__(self, surface, x, y, width, height, cols, rows, blue, green, red, bg, line):
        self.rad = 10
        self.surface = surface
        self.x = x - self.rad
        self.y = y
        self.swidth = width
        self.sheight = height
        self.cols = cols
        self.rows = rows
        self.blue = blue
        self.green = green
        self.red = red
        self.bg = bg
        self.line = line
        self.col = (142, 135, 123)
        self.outline_col = (100, 100, 100)
        self.rect = pygame.Rect(self.x, self.y, self.rad * 2, self.rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = False
        self.start = False
        self.win = False

    def move(self, wall):
        coll = 5
        wall_des = 1
        row_cnt = 0
        for row in wall.blocks:
            item_cnt = 0
            for item in row:
                if self.rect.colliderect(item[0]):
                    if abs(self.rect.bottom - item[0].top) < coll and self.speed_y > 0:
                        self.speed_y *= -1
                    if abs(self.rect.top - item[0].bottom) < coll and self.speed_y < 0:
                        self.speed_y *= -1
                    if abs(self.rect.left - item[0].right) < coll and self.speed_x > 0:
                        self.speed_x *= -1
                    if abs(self.rect.right - item[0].left) < coll and self.speed_x < 0:
                        self.speed_x *= -1

                    if wall.blocks[row_cnt][item_cnt][1] > 1:
                        wall.blocks[row_cnt][item_cnt][1] -= 1
                    else:
                        wall.blocks[row_cnt][item_cnt][0] = (0, 0, 0, 0)

                if wall.blocks[row_cnt][item_cnt][0] != (0, 0, 0, 0):
                    wall_des = 0
                item_cnt += 1
            row_cnt += 1

        if wall_des == 1:
            self.win = True

        if self.rect.left < 0 or self.rect.right > self.swidth:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > self.sheight:
            self.game_over = True

        if self.rect.colliderect(self.line):
            if abs(self.rect.bottom - self.line.rect.top) < coll and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += self.line.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                if self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1
        if self.start:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

    def draw(self):
        pygame.draw.circle(self.surface, self.col, (self.rect.x + self.rad, self.rect.y + self.rad), self.rad)
        pygame.draw.circle(self.surface, self.outline_col, (self.rect.x + self.rad, self.rect.y + self.rad), self.rad, 3)

    def reset(self):
        self.col = (142, 135, 123)
        self.outline_col = (100, 100, 100)
        self.rect = pygame.Rect(self.x, self.y, self.rad * 2, self.rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = False
        self.start = False

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Quadro')
        self.width = 600
        self.height = 600
        self.bg_color = (234, 218, 184)
        self.red = (242, 85, 96)
        self.green = (86, 174, 87)
        self.blue = (69, 177, 232)
        self.text_col = (78, 81, 139)
        self.cols = 6
        self.rows = 6
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.SysFont('Constantia', 50)
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.blocks = Block(self.surface, self.width, self.height, self.cols, self.rows, self.blue, self.green, self.red, self.bg_color)
        self.line = Line(self.surface, self.width, self.height, self.cols, self.rows, self.blue, self.green, self.red, self.bg_color)
        self.ball = Ball(self.surface, self.line.x + self.line.width // 2, self.line.y - self.line.height, self.width, self.height, self.cols,
                self.rows, self.blue, self.green, self.red, self.bg_color, self.line)
        self.rungame = True
        self.start_game = False

    def draw_element(self):
        self.blocks.draw_block()
        self.line.draw()
        self.ball.draw()

    def move_element(self):
        self.line.move()
        self.ball.move(self.blocks)

    def reset(self):
        self.ball.reset()
        self.line.reset()

    def show_game_over(self):
        if self.ball.game_over:
            text = self.font.render("Game Over!!", 1, self.text_col)
            text_sur = text.get_rect(center=(300, 400))
            self.surface.blit(text, text_sur)
            self.line.move_true = False
            self.start_game = False

    def show_win(self):
        if self.ball.win:
            text = self.font.render("You Win!!", 1, self.text_col)
            text_sur = text.get_rect(center=(300, 400))
            self.surface.blit(text, text_sur)
            self.line.move_true = False
            self.start_game = False

    def play(self):
        self.clock.tick(self.fps)
        self.surface.fill(self.bg_color)
        self.draw_element()
        self.move_element()
        self.show_game_over()
        self.show_win()

    def run(self):
        self.blocks.create_block()

        while self.rungame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rungame = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.ball.start and not self.start_game:
                        self.ball.start = True
                        self.start_game = True
                    elif not self.start_game:
                        self.ball.start = False
                        self.reset()

            self.play()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

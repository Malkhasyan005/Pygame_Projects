import random
import sys
try:
    import pygame
    from pygame.math import Vector2
except ImportError as err:
    print("Please install pygame module")
    sys.exit()

class Bomb:
    def __init__(self, surface):
        self.surface = surface
        self.block_size = 40
        self.block_count = 20
        self.img = pygame.image.load("img/bomb.png")
        self.x = random.randint(0, self.block_count - 1)
        self.y = random.randint(0, self.block_count - 1)
        self.coordinate = Vector2(self.x, self.y)

    def draw(self):
        x = self.coordinate.x * self.block_size
        y = self.coordinate.y * self.block_size
        bomb = pygame.Rect(x, y, self.block_size, self.block_size)
        self.surface.blit(self.img, bomb)

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.block_size = 40
        self.block_count = 20
        self.img = pygame.image.load("img/apple.png")
        self.x = random.randint(0, self.block_count - 1)
        self.y = random.randint(0, self.block_count - 1)
        self.coordinate = Vector2(self.x, self.y)

    def draw(self):
        block = pygame.Rect(int(self.coordinate.x * self.block_size), int(self.coordinate.y * self.block_size),
                                self.block_size, self.block_size)
        self.surface.blit(self.img, block)

    def randomize(self):
        self.x = random.randint(0, self.block_count - 1)
        self.y = random.randint(0, self.block_count - 1)
        self.coordinate = Vector2(self.x, self.y)

class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.block_size = 40
        self.block_count = 20
        self.add = False
        self.coordinates = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(0, 0)
        self.head = pygame.image.load('img/head_right.png').convert_alpha()
        self.tail = pygame.image.load('img/tail_left.png').convert_alpha()

        self.head_up = pygame.image.load('img/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('img/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('img/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('img/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('img/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('img/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('img/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('img/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('img/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('img/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('img/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('img/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('img/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('img/body_bl.png').convert_alpha()

    def draw(self):
        self.update_head()
        self.update_tail()

        for ind, coord in enumerate(self.coordinates):
            x = int(coord.x * self.block_size)
            y = int(coord.y * self.block_size)
            block = pygame.Rect(x, y, self.block_size, self.block_size)

            if ind == 0:
                self.surface.blit(self.head, block)
            elif ind == len(self.coordinates) - 1:
                self.surface.blit(self.tail, block)
            else:
                block_previous = self.coordinates[ind + 1] - coord
                block_next = self.coordinates[ind - 1] - coord

                if block_next.y == block_previous.y:
                    self.surface.blit(self.body_horizontal, block)
                elif block_next.x == block_previous.x:
                    self.surface.blit(self.body_vertical, block)
                else:
                    if block_previous.x == -1 and block_next.y == 1 or block_previous.y == 1 and block_next.x == -1:
                        self.surface.blit(self.body_bl, block)
                    elif block_previous.x == 1 and block_next.y == 1 or block_previous.y == 1 and block_next.x == 1:
                        self.surface.blit(self.body_br, block)
                    elif block_previous.x == -1 and block_next.y == -1 or block_previous.y == -1 and block_next.x == -1:
                        self.surface.blit(self.body_tl, block)
                    elif block_previous.x == 1 and block_next.y == -1 or block_previous.y == -1 and block_next.x == 1:
                        self.surface.blit(self.body_tr, block)

    def update_head(self):
        head_pos = self.coordinates[1] - self.coordinates[0]
        if head_pos == Vector2(-1, 0):
            self.head = self.head_right
        elif head_pos == Vector2(1, 0):
            self.head = self.head_left
        elif head_pos == Vector2(0, -1):
            self.head = self.head_down
        elif head_pos == Vector2(0, 1):
            self.head = self.head_up

    def update_tail(self):
        tail_pos = self.coordinates[-2] - self.coordinates[-1]
        if tail_pos == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_pos == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_pos == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_pos == Vector2(0, -1):
            self.tail = self.tail_down

    def move(self):
        if self.add:
            new_coord = self.coordinates[:]
            new_coord.insert(0, new_coord[0] + self.direction)
            self.coordinates = new_coord
            self.add = False
        else:
            new_coord = self.coordinates[:-1]
            new_coord.insert(0, new_coord[0] + self.direction)
            self.coordinates = new_coord

    def add_block(self):
        self.add = True

class Game:
    def __init__(self):
        pygame.init()
        self.block_size = 40
        self.block_count = 20
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.block_size * self.block_count, self.block_size * self.block_count))
        self.food = Food(self.surface)
        self.snake = Snake(self.surface)
        self.bomb = Bomb(self.surface)
        self.start = False
        self.SCREEN_UPDATE = pygame.USEREVENT
        self.fps = 200
        self.running = True
        self.pause = False
        pygame.time.set_timer(self.SCREEN_UPDATE, self.fps)
        self.font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)
        self.font2 = pygame.font.Font('font/PoetsenOne-Regular.ttf', 50)

    def draw_score(self):
        score_text = str(len(self.snake.coordinates) - 3)
        score_surface = self.font.render(score_text, True, (56, 74, 12))
        score_x = int(self.block_size * self.block_count - 60)
        score_y = int(self.block_size * self.block_count - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.food.img.get_rect(midright=(score_rect.left, score_rect.centery))

        self.surface.blit(score_surface, score_rect)
        self.surface.blit(self.food.img, apple_rect)

    def eat_food(self):
        if self.snake.coordinates[0] == self.food.coordinate:
            self.food.randomize()
            self.snake.add_block()
            self.fps -= 10

        for block in self.snake.coordinates[1:]:
            if block == self.food.coordinate or self.food.coordinate == self.bomb.coordinate:
                self.food.randomize()

    def eat_bomb(self):
        if self.bomb.coordinate == self.snake.coordinates[0]:
            self.game_over()

    def show_game_over(self):
        game_over = str("Game Over")
        game_over_surface = self.font2.render(game_over, True, (56, 74, 12))
        coord = game_over_surface.get_rect(center=(400, 400))

        self.surface.blit(game_over_surface, coord)

    def game_over(self):
        self.pause = True
        self.show_game_over()

    def fail(self):
        if not 0 <= self.snake.coordinates[0].x < self.block_count or not 0 <= self.snake.coordinates[0].y < self.block_count:
            self.game_over()

        for coord in self.snake.coordinates[1:]:
            if coord == self.snake.coordinates[0]:
                self.game_over()

    def draw_element(self):
        self.food.draw()
        self.snake.draw()
        self.bomb.draw()

    def play(self):
        self.surface.fill((175, 215, 70))
        self.draw_element()
        self.eat_food()
        self.draw_score()
        self.eat_bomb()
        self.fail()


    def start_game(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.SCREEN_UPDATE:
                    if self.start:
                        self.snake.move()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.start = True
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0, 1)
                    elif event.key == pygame.K_RIGHT:
                        self.start = True
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1, 0)
                    elif event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1, 0)

            if not self.pause:
                self.play()

            self.clock.tick(30)
            pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.start_game()
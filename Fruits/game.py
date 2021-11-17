import random
import time
import sys
try:
    import pygame
    from pygame.math import Vector2
except ImportError as err:
    print("Please install pygame module")
    sys.exit()

class Basket:
    def __init__(self, surface):
        self.surface = surface
        self.x = 368
        self.y = 730
        self.pos = Vector2(self.x, self.y)
        self.direction = Vector2(0, 0)
        self.image = pygame.image.load('img/basket.png')

    def draw(self):
        self.surface.blit(self.image, self.pos)

    def move(self):
        self.pos += self.direction

class Fruit:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, 768)
        self.y = 0
        self.pos = Vector2(self.x, self.y)
        self.direction = Vector2(0, 0.2)
        self.index = 0
        self.is_rand = True
        self.images = [pygame.image.load(f'img/fruits/{i}.png') for i in  range(1,6)]

    def get_random_image(self):
        if self.is_rand:
            self.index = random.randint(0, len(self.images) - 1)
            self.pos.x = random.randint(0, 768)
            self.is_rand = False

    def draw(self):
        self.get_random_image()
        self.surface.blit(self.images[self.index], self.pos)

    def move(self):
        self.pos += self.direction

    def draw_element_new_pos(self):
        self.x = random.randint(0, 768)
        self.y = 0
        self.pos = Vector2(self.x, self.y)

class Game:
    def __init__(self):
        pygame.init()
        self.height = 800
        self.width = 800
        self.score = 0
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.mouse_pos = None
        self.basket = Basket(self.surface)
        self.fruit = Fruit(self.surface)
        self.font = pygame.font.SysFont('comicsans', 80)
        self.font2 = pygame.font.SysFont('comicsans', 30)
        self.font3 = pygame.font.SysFont('comicsans', 50)
        self.img_fruits = pygame.image.load('img/fruits/fruit.png')
        self.score_show = True
        self.start_game = False
        self.show_game_over = False
        self.running = True

    def show_game_over_fn(self):
        game_over_text = self.font.render("Game Over", 1, (0, 0, 0))
        game_over_text_surface = game_over_text.get_rect(center=(self.width//2, 370))
        show_score = self.font2.render(f"You have collected {self.score} fruits", 1, (0, 0, 0))
        show_score_surface = show_score.get_rect(center=(self.width//2, 450))

        self.surface.blit(game_over_text, game_over_text_surface)
        self.surface.blit(show_score, show_score_surface)

    def show_score(self):
        score = self.font2.render(f'{self.score}', 1, (0, 0, 0))
        score_surface = score.get_rect(center=(770, 32))
        img = self.img_fruits.get_rect(center=(740, 32))

        self.surface.blit(self.img_fruits, img)
        self.surface.blit(score, score_surface)

    def is_basket_in_the_end(self):
        if 0 >= self.basket.pos.x:
            self.basket.pos.x = 0
        if self.basket.pos.x > self.width - 64:
            self.basket.pos.x = self.width - 64

    def game_over(self):
        if self.fruit.pos.y >= self.basket.pos.y - 15:
            self.score_show = False
            self.show_game_over = True
            self.start_game = False
            self.fruit.direction.y = 0
            self.show_game_over_fn()

    def start_game2(self):
        self.surface.fill((255, 255, 255))
        play = pygame.Rect((275, 362), (250, 75))
        play_text = self.font3.render('Play', 1, (0, 0, 0))
        play_text_surface = play_text.get_rect(center=(400, 400))

        self.surface.blit(play_text, play_text_surface)
        pygame.draw.rect(self.surface, (0, 0, 0), play, 4)

    def restart(self):
        self.score = 0
        self.draw_element()
        self.fruit.direction.y = 0.2
        self.basket.pos = Vector2(368, 730)
        self.show_game_over = False
        self.score_show = True
        self.fruit.draw_element_new_pos()

    def is_in_button(self):
        if 275 < self.mouse_pos.x < 525:
            if 362 < self.mouse_pos.y < 437:
                self.start_game = True

    def is_fruit_in_basket(self):
        if self.fruit.pos.y >= self.basket.pos.y - 28:
            if self.basket.pos.x - 16 <= self.fruit.pos.x <= self.basket.pos.x + 60:
                self.is_score_5()
                self.fruit.pos.y = 0
                self.fruit.is_rand = True
                self.score += 1

    def is_score_5(self):
        if self.score % 5 == 0:
            self.fruit.direction.y += 0.1

    def move_element(self):
        if self.start_game:
            self.basket.move()
            self.fruit.move()

    def draw_element(self):
        self.surface.fill((255, 255, 255))
        self.basket.draw()
        self.fruit.draw()

    def play(self):
        self.draw_element()
        self.is_basket_in_the_end()
        self.move_element()
        self.is_fruit_in_basket()
        if not self.start_game and not self.show_game_over:
            self.start_game2()
        if self.score_show and self.start_game:
            self.show_score()
        self.game_over()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if not self.show_game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.basket.direction = Vector2(-0.5, 0)
                        if event.key == pygame.K_RIGHT:
                            self.basket.direction = Vector2(0.5, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        self.mouse_pos = Vector2(x, y)
                        self.is_in_button()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            self.basket.direction = Vector2(0, 0)
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.restart()

            self.play()

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
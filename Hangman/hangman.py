import random

try:
    import pygame
except:
    print("Please import pygame module")
from pygame.math import Vector2
import time
import math

class Game:
    def __init__(self, fcnt):
        pygame.init()
        self.width = 1000
        self.height = 700
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.radius = 30
        self.margin = 15
        self.mouse_pos = Vector2()
        self.letter_font = pygame.font.SysFont('comicsans', 40)
        self.letter_font_50 = pygame.font.SysFont('comicsans', 50)
        self.letter_font_100 = pygame.font.SysFont('comicsans', 100)
        self.game_over = False
        self.mistake = 0
        self.words = fcnt
        self.dis_word = ""
        self.word = self.words[random.randint(0, 6)]
        self.word_list = []
        self.letters = []
        self.images = []

    def win(self):
        if self.word == "".join(self.dis_word.split()):
            self.game_over = True
            text = self.letter_font_100.render("You Winnnn!!", 1, (0, 0, 0))
            text_surface = text.get_rect(center=(self.width // 2, self.height // 2))
            self.surface.blit(text, text_surface)

    def restart(self):
        self.game_over = False
        self.word_list.clear()
        self.mistake = 0
        self.word = self.words[random.randint(0, 6)]
        for let in self.letters:
            let[2] = True

    def show_game_over(self):
        if self.mistake == 6:
            self.game_over = True
            text = self.letter_font_100.render("Game Over!!", 1, (0, 0, 0))
            text_surface = text.get_rect(center=(self.width // 2, self.height // 2))
            self.surface.blit(text, text_surface)


    def is_let_in_word(self, let):
        if let not in self.word:
            self.mistake += 1

    def write_word(self):
        self.dis_word = ""
        for let in self.word:
            if let in self.word_list:
                self.dis_word += let + " "
            else:
                self.dis_word += "_ "

    def draw_word(self):
        text = self.letter_font_50.render(self.dis_word, 1, (0, 0, 0))
        self.surface.blit(text, (500, 200))

    def is_in_letter(self):
        for letter in self.letters:
            dis = math.sqrt((letter[0].x - self.mouse_pos.x)**2 + (letter[0].y - self.mouse_pos.y)**2)
            if letter[2]:
                if dis < self.radius:
                    letter[2] = False
                    self.word_list.append(letter[1])
                    self.is_let_in_word(letter[1])

    def get_images(self):
        for ind in range(7):
            img = pygame.image.load(f'hangman/hangman{ind}.png')
            self.images.append(img)

    def get_letter(self):
        start_x = round((self.width - (self.radius * 2 + self.margin) * 13) / 2)
        start_y = 500
        for i in range(26):
            x = start_x + self.margin * 2 + ((self.radius * 2 + self.margin) * (i % 13))
            y = start_y + ((i // 13) * (self.margin + self.radius * 2))
            let = chr(65 + i)
            self.letters.append([Vector2(x, y), let, True])

    def draw(self):
        for el in self.letters:
            if el[2]:
                pygame.draw.circle(self.surface, (0, 0, 0), el[0], self.radius, 3)
                text = self.letter_font.render(el[1], 1, (0, 0, 0))
                text_surface = text.get_rect(center=el[0])
                self.surface.blit(text, text_surface)

    def get(self):
        self.get_images()
        self.get_letter()

    def play(self):
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.images[self.mistake], (150, 100))
        self.write_word()
        self.draw_word()
        self.draw()
        self.win()
        self.show_game_over()

    def run(self):
        running_game = True

        while running_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                if not self.game_over:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        self.mouse_pos = Vector2(x, y)
                        self.is_in_letter()
                if self.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.restart()

            self.play()

            pygame.display.update()


def get_words():
    with open("Categotis.txt") as f:
       return f.read().split()

if __name__ == '__main__':
    game = Game(get_words())
    game.get()
    game.run()

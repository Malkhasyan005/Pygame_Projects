# Piano Game

try:
    import pygame
except:
    print("Please import pygame module")
from pygame.math import Vector2
from pygame.locals import *
from pygame import mixer
import time
import math
import random

class Block:
    def __init__(self, surface):
        self.surface = surface
        self.width = 125
        self.height = 200
        self.color = (0, 0, 0)
        self.color2 = (180,180,180)
        self.x = 0
        self.y = -self.height
        self.click = False
        self.pos = Vector2(self.x, self.y)
        self.block = pygame.Rect(self.pos, (self.width, self.height))
    
    def draw(self, n):
        self.pos.x = self.width * n

    def move(self):
        if not self.click:
            block = pygame.Rect(self.pos, (self.width, self.height))
            pygame.draw.rect(self.surface, self.color, block)
        else:
            block = pygame.Rect(self.pos, (self.width, self.height))
            pygame.draw.rect(self.surface, self.color2, block)

    def click_block(self, pos):
        if pos[0] in range(int(self.pos.x), int(self.pos.x + self.width)):
            if pos[1] in range(int(self.pos.y), int(self.pos.y + self.height)):
                self.click = True
                return False
        return True



class Game:
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 800
        self.bg_color = (255, 255, 255)
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.ind = [0, 1, 2, 3, 0, 1, 2, 1, 3, 0]
        self.blocks = []
        self.block = 0
        self.fps = 75
        self.mouse_pos = None
        self.clock=pygame.time.Clock()
        self.game_over = False
        self.rungame = True
        mixer.music.load('frog.wav')
        mixer.music.play(-1)
    
    def play(self):
        pass

    def run(self):
        
        while self.rungame:
            for i in self.ind:
                self.blocks.append(Block(self.surface))
                self.blocks[-1].draw(random.randint(0, 3))

                for j in range(self.height//(4 * 4)):
                    if self.rungame:
                        self.clock.tick(self.fps)
                        self.surface.fill(self.bg_color)

                        for k in range(len(self.blocks)):
                            self.blocks[k].pos.y += 4
                            self.blocks[k].move()
                            
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                self.rungame = False

                            if event.type == MOUSEBUTTONDOWN:
                                self.mouse_pos = pygame.mouse.get_pos()
                                self.game_over = self.blocks[self.block].click_block(self.mouse_pos)
                                if self.game_over:
                                    self.rungame = False
                                self.block += 1
                                self.fps += 1
                            
                        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

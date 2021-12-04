try:
    import pygame
except:
    print("Please install pygame")
import utils
from pygame.math import Vector2

class Game:
    def __init__(self):
        pygame.init()
        self.width = 1200
        self.height = 600
        self.questions = None
        self.answer = None
        self.ind = 0
        self.bonus = 0
        self.block_pos = [Vector2(50, 350), Vector2(650, 350), Vector2(50, 500), Vector2(650, 500)]
        self.mouse_pos = None
        self.font = pygame.font.SysFont('comicsans', 30)
        self.font1 = pygame.font.SysFont('comicsans', 50)
        self.click = True
        self.show_answer = False
        self.coorect_answer_color = (17, 125, 2)
        self.wrong_answer_color = (120, 14, 16)
        self.bg_color = (2, 60, 153)
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.rungame = True
        self.fifty = True
        self.friend = True
        self.audience = False
        self.finish = False

    def get_questions(self):
        self.questions = utils.get_questions("questions.txt")

    def shuffle_answ(self):
        if self.click and self.ind < 7:
            self.answer = utils.shuffle_answers(self.questions[self.ind])
            self.click = False

    def show_correct_answ(self, ind):
        self.surface.fill(self.bg_color)
        block = pygame.Rect(self.block_pos[ind], (500, 75))
        pygame.draw.rect(self.surface, self.coorect_answer_color, block, 0, 50)
        self.draw_element()
        self.show_answer = True

    def show_wrong_answ(self, ind):
        self.surface.fill(self.bg_color)
        block = pygame.Rect(self.block_pos[ind], (500, 75))
        pygame.draw.rect(self.surface, self.wrong_answer_color, block, 0, 50)
        block1 = pygame.Rect(self.block_pos[self.answer.index(self.questions[self.ind].corrans)], (500, 75))
        pygame.draw.rect(self.surface, self.coorect_answer_color, block1, 0, 50)
        self.draw_element()
        self.show_answer = True


    def is_correct(self, ind):
        if self.answer[ind] == self.questions[self.ind].corrans:
            self.show_correct_answ(ind)
            self.bonus += int(self.questions[self.ind].bonus)
        else:
            self.show_wrong_answ(ind)

    def choose_answer(self):
        if self.mouse_pos.x in range(50, 550) and self.mouse_pos.y in range(350, 425):
            self.is_correct(0)
            self.ind += 1
            self.click = True
        elif self.mouse_pos.x in range(650, 1150) and self.mouse_pos.y in range(350, 425):
            self.is_correct(1)
            self.ind += 1
            self.click = True
        elif self.mouse_pos.x in range(50, 550) and self.mouse_pos.y in range(500, 575):
            self.is_correct(2)
            self.ind += 1
            self.click = True
        elif self.mouse_pos.x in range(650, 1150) and self.mouse_pos.y in range(500, 575):
            self.is_correct(3)
            self.ind += 1
            self.click = True
    
    def show_helps(self):
        pygame.draw.circle(self.surface, (0, 0, 0), (1150, 50), 35, 3)
        pygame.draw.circle(self.surface, (0, 0, 0), (1065, 50), 35, 3)
        pygame.draw.circle(self.surface, (0, 0, 0), (980, 50), 35, 3)

        fifty = self.font.render('50/50', 1, (0, 0, 0))
        fifty_surface = fifty.get_rect(center=(1150, 50))

        friend = self.font.render('F/H', 1, (0, 0, 0))
        friend_surface = friend.get_rect(center=(1065, 50))

        audience = self.font.render('H/H', 1, (0, 0, 0))
        audience_surface = audience.get_rect(center=(980, 50))

        if self.fifty:
            self.surface.blit(fifty, fifty_surface)
        if self.friend:
            self.surface.blit(friend, friend_surface)
        if self.audience:
            self.surface.blit(audience, audience_surface)

    def show_answers(self):
        answ1 = self.font.render(f"A: {self.answer[0]}", 1, (0, 0, 0))
        answ2 = self.font.render(f"B: {self.answer[1]}", 1, (0, 0, 0))
        answ3 = self.font.render(f"C: {self.answer[2]}", 1, (0, 0, 0))
        answ4 = self.font.render(f"D: {self.answer[3]}", 1, (0, 0, 0))

        answ1_surface = answ1.get_rect(topleft=(80, 375))
        answ2_surface = answ2.get_rect(topleft=(680, 375))
        answ3_surface = answ3.get_rect(topleft=(80, 525))
        answ4_surface = answ4.get_rect(topleft=(680, 525))
        
        self.surface.blit(answ1, answ1_surface)
        self.surface.blit(answ2, answ2_surface)
        self.surface.blit(answ3, answ3_surface)
        self.surface.blit(answ4, answ4_surface)


    def drwa_answer_blocks(self):
        answblock1 = pygame.Rect(self.block_pos[0], (500, 75))
        answblock2 = pygame.Rect(self.block_pos[1], (500, 75))
        answblock3 = pygame.Rect(self.block_pos[2], (500, 75))
        answblock4 = pygame.Rect(self.block_pos[3], (500, 75))


        pygame.draw.rect(self.surface, (0, 0, 0), answblock1, 4, 50)
        pygame.draw.rect(self.surface, (0, 0, 0), answblock2, 4, 50)
        pygame.draw.rect(self.surface, (0, 0, 0), answblock3, 4, 50)
        pygame.draw.rect(self.surface, (0, 0, 0), answblock4, 4, 50)

    def show_answ(self):
        quest = self.font.render(f"{self.questions[self.ind].question}", 1, (0, 0, 0))
        quest_surface = quest.get_rect(center=(self.width//2, self.height//3))

        self.surface.blit(quest, quest_surface)

    def show_final_bonus(self):
        self.surface.fill(self.bg_color)
        finish = self.font1.render(f"Game finished. You have {self.bonus} points", 1, (0, 0, 0))
        finish_surface = finish.get_rect(center=(self.width//2, self.height//2))

        self.surface.blit(finish, finish_surface)
        self.finish = True


    def draw_element(self):
        self.drwa_answer_blocks()
        self.show_answ()
        self.show_answers()
        self.show_helps()

    def play(self):
        if self.ind >= 7 and not self.show_answer:
            self.show_final_bonus()
        if not self.show_answer and not self.finish:
            self.surface.fill(self.bg_color)
            self.shuffle_answ()
            self.draw_element()

    def run(self):
        self.get_questions()
        while self.rungame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rungame = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.show_answer:
                    x, y = pygame.mouse.get_pos()
                    self.mouse_pos = Vector2(x, y)
                    self.choose_answer()
                if event.type == pygame.KEYDOWN and self.show_answer and not self.finish:
                    if event.key == pygame.K_SPACE:
                            self.show_answer = False
            
            self.play()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()

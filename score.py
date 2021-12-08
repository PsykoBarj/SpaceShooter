import pygame

class show_score:
    def __init__(self, x, y):
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score = self.font.render("Score : " + str(self.score_value), True, (255,255,255))
        self.score
        self.rect = self.score.get_rect(x=10, y=10)

    def update(self):
        self.score = self.font.render("Score : " + str(self.score_value), True, (255,255,255))
        
    def draw(self, screen):
        screen.blit(self.score, self.rect)
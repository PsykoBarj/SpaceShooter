import pygame

class Life:
    def __init__(self, x, y):
        self.life_value = 3
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.life = self.font.render("Vie(s) : " + str(self.life_value), True, (255,255,255))
        self.life
        self.rect = self.life.get_rect(x=10, y=50)

    def update(self):
        self.life = self.font.render("Vie(s) : " + str(self.life_value), True, (255,255,255))
        
    def draw(self, screen):
        screen.blit(self.life, self.rect)
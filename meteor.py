import pygame
import random

class Meteor:
    def __init__(self):
        self.image = pygame.image.load(".\Images\meteor.png").convert_alpha()
        self.surf = pygame.Surface((192,74))
        self.rect = self.surf.get_rect(center = (random.randint(30,1010), (random.randint(-200,0))))
        self.speed = 1

    def move(self, destroyed):
        self.rect.move_ip(0,self.speed)
        if(self.rect.y > 650) or destroyed == True:
            self.rect.center = (random.randint(30,1010), (random.randint(-200,0)))
            self.speed += 0.15
            if self.speed >= 3.0:
                self.speed = 3.0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

import pygame
import random

class Meteor:
    def __init__(self):
        self.image = pygame.image.load(".\Images\enemy.png")
        self.surf = pygame.Surface((30,30))
        self.rect = self.surf.get_rect(center = (random.randint(30,1060), (random.randint(-200,0))))

    def move(self, destroyed):
        speed = 1
        self.rect.move_ip(0,speed)
        if(self.rect.y > 660) or destroyed == True:
            self.rect.center = (random.randint(30,1060), (random.randint(-200,0)))
            speed = speed + 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)
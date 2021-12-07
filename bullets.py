import pygame

class Bullets:
    def __init__(self, x, y):
        self.image = pygame.image.load(".\Images\Bullets.png")
        self.image
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 10
        self.velocity = [0]

    def move(self):
        self.rect.move_ip(0, self.velocity[0] * self.speed)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
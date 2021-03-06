import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load(".\Images\Spaceship.png")
        self.image
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 6
        self.velocity = [0, 0]

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
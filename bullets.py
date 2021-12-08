import pygame
from player import Player
from pygame import mixer

class Bullets:
    def __init__(self, x, y):
        self.image = pygame.image.load(".\Images\Bullets.png")
        self.image
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 10
        self.velocity = [0]
        self.state = ""
        self.SHOOT_SOUND = pygame.mixer.Sound('./Sons/shoot.wav')
        self.SHOOT_SOUND.set_volume(0.2)
        self.HIT_SOUND = pygame.mixer.Sound('./Sons/hit.wav')
        self.HIT_SOUND.set_volume(0.5)

    def move(self):
        self.rect.move_ip(0, self.velocity[0] * self.speed)
    
    def draw(self, screen):
        if self.state == "fire":
            screen.blit(self.image, self.rect)
import pygame
from pygame import mixer
from player import Player
from score import show_score
from bullets import Bullets
from meteor import Meteor

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        px = 500
        py = 500
        self.player = Player(px, py)
        self.score = show_score(10,10)
        self.bullets = Bullets(self.player.rect.x, self.player.rect.y)
        self.bullets.state = "ready"

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.bullets.state == "ready":
                        self.bullets.rect.x = self.player.rect.x
                        self.bullets.rect.y = self.player.rect.y + 10
                        self.bullets.state = "fire"
                        self.bullets.SHOOT_SOUND.play()
                        self.bullets.velocity[0] = -1

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif key[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

        if key[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif key[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0

        if self.player.rect.x <= 0:
            self.player.rect.x = 0
        if self.player.rect.x >= 1010:
            self.player.rect.x = 1010
        if self.player.rect.y <= 0:
            self.player.rect.y = 0
        if self.player.rect.y >= 650:
            self.player.rect.y = 650
        
                

    def update(self):
        self.player.move()
        self.bullets.move()
        if self.bullets.rect.y <= -10:
            self.bullets.rect.x = self.player.rect.x
            self.bullets.rect.y = self.player.rect.y
            self.bullets.state = "ready"
        

    def display(self):
        self.screen.fill("black")
        self.player.draw(self.screen)
        self.bullets.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(300)

pygame.init()
screen = pygame.display.set_mode((1080,720))
game = Game(screen)
game.run()

pygame.quit()
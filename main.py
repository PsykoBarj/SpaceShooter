import pygame
from player import Player

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(500, 500)

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

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

    def update(self):
        self.player.move()

    def display(self):
        self.screen.fill("black")
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((1080,720))
game = Game(screen)
game.run()

pygame.quit()
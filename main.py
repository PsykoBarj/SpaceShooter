import pygame

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        pass
    def display(self):
        pass
    def run(self):
        pass

pygame.init()
screen = pygame.display.set_mode((1080,720))
game = Game(screen)
game.run()

pygame.quit()
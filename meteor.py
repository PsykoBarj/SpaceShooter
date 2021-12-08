import pygame

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\Images\enemy.png")
        self.surf = pygame.Surface((30,30))
        self.rect = self.surf.get_rect(center = (random.randint(40,460), (random.randint(-100,0))))

    def move(self, score, destroyed):
        self.rect.move_ip(0,speed)
        if(self.rect.x > 660) or destroyed == True:
            self.rect.center = (random.randint(30,460), (random.randint(-100,0)))
            score += 1

        return score
               
    def draw(self, surface):
        surface.blit(self.image, self.rect)
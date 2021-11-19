import pygame

class Spaceship(object):
    def __init__(self):
        self.image = pygame.image.load('P:\Documents\ProjetJeu\Spaceship.png').convert_alpha()
        self.x = 250
        self.y = 250
    def handle_keys(self):
        key = pygame.key.get_pressed()
        speed = 5 # speedance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += speed # move down
        elif key[pygame.K_UP]: # up key
            self.y -= speed # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += speed # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= speed # move left
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

pygame.init()

fenetre = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Projet shooter")

run = True

fond = pygame.image.load("P:\Documents\ProjetJeu\Background.png").convert()
fenetre.blit(fond, (0,0))

while run:

    spaceship = Spaceship()
    clock = pygame.time.Clock()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False

    spaceship.handle_keys()
    spaceship.draw(fenetre)              
    pygame.display.update()
    clock.tick(40) 

pygame.quit()
 
import pygame 
pygame.init()
 
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Projet shooter")

run = True

fond = pygame.image.load(".\Images\Background.jpg").convert()

bullets = []
bulletpicture = pygame.image.load(".\SpaceShooter\Images\bulletsspaceship.png").convert_alpha()

class Spaceship(object):
    def __init__(self):
        self.image = pygame.image.load('.\Images\Spaceship.png').convert_alpha()
        self.x = 200
        self.y = 200
    def key(self):
        keys = pygame.key.get_pressed()
        vel = 10
        if keys[pygame.K_LEFT] and self.x>0:
            self.x -= vel
        if keys[pygame.K_RIGHT] and self.x<500-80:
            self.x += vel 
        if keys[pygame.K_UP] and self.y>0:
            self.y -= vel  
        if keys[pygame.K_DOWN] and self.y<500-80:
            self.y += vel
    def draw(self, surface):
        surface.blit(self.image, (self.x,self.y))

spaceship = Spaceship()

while run:
    
    pygame.time.delay(10)
        
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            shot.play()
            bullets.append([event.pos[0]-32, 500])

    clock.tick(60)

    mx, my = pygame.mouse.get_pos()

    for b in range(len(bullets)):
        bullets[b][0] -= 10

    # Iterate over a slice copy if you want to mutate a list.
    for bullet in bullets[:]:
        if bullet[0] < 0:
            bullets.remove(bullet)

    spaceship.key()
    win.blit(fond, (0,0))
    for bullet in bullets:
        screen.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
    spaceship.draw(win)
    pygame.display.update() 
   
pygame.quit()
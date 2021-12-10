import pygame, sys
from pygame import *
from pygame import mixer
from player import Player
from score import show_score
from life import Life
from bullets import Bullets
from meteor import Meteor

pygame.init()
screen = pygame.display.set_mode((1080, 720))
font = pygame.font.SysFont('Cooper black', 30)
ck = pygame.time.Clock()
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
 
    click = False 
    menu = True
    while menu:
 
        screen.fill((0,0,0))
        draw_text('Start Menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(525, 250, 200, 50)
        text1 = font.render('Jouer', False, (255,255,255))
 
        if button_1.collidepoint ((mx, my)) and click == True :
            menu = False

        pygame.draw.rect(screen, (0, 0, 0), button_1)
        screen.blit(text1, (583, 255))
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        ck.tick(60)

main_menu()

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.background = pygame.image.load('.\Images\Background.jpg')
        self.running = True
        self.clock = pygame.time.Clock()
        px = 500
        py = 500
        self.player = Player(px, py)
        self.meteor = Meteor()
        self.score = show_score(10,10)
        self.life = Life(10, 50)
        self.bullets = Bullets(2000, 2000)
        self.bullets.state = "ready"
        self.BACKGROUND_SOUND = pygame.mixer.Sound('./Sons/BackgroundMusic.mp3')
        self.BACKGROUND_SOUND.set_volume(0.3)
        self.BACKGROUND_SOUND.play(loops=0, maxtime=0, fade_ms=0)

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.bullets.state == "ready":
                        self.bullets.rect.x = self.player.rect.x
                        self.bullets.rect.y = self.player.rect.y + 15
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
        if self.meteor.rect.colliderect(self.bullets.rect):
            self.meteor.move(True)
            self.score.score_value += 1
            self.bullets.velocity[0] = 0
            self.bullets.rect.x = 2000
            self.bullets.rect.y = 2000
            self.bullets.state = "ready"
            self.bullets.HIT_SOUND.play()
        if (self.meteor.rect.y > 610):
            self.meteor.rect.y = 2000
            self.life.life_value -= 1
            if self.life.life_value == 0:
                self.running = False
        self.score.update()
        self.life.update()
        self.meteor.move(False)
        self.bullets.move()
        if self.bullets.rect.y <= -10:
            self.bullets.state = "ready"
        

    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        self.meteor.draw(self.screen)
        self.bullets.draw(self.screen)
        self.score.draw(self.screen)
        self.life.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(300)

pygame.init()
screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Space Shooter")
game = Game(screen)
game.run()

pygame.quit()

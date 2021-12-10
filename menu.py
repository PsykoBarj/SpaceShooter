import pygame

class Menu():

    def __init__(self):
        pass

    def draw_text(self, text, font, color, screen, x, y):
        self.textobj = font.render(text, 1, color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)
        self.draw_text = (text, font, color, screen, x, y)

    def update(self):
        self.click = False 
        self.menu = True
        while self.menu:
 
            self.screen.fill((0,0,0))
            self.draw_text('Start Menu', font, (255, 255, 255), screen, 20, 20)
 
            self.mx, self.my = pygame.mouse.get_pos()

            self.button_1 = pygame.Rect(525, 250, 200, 50)
            self.text1 = self.font.render('Jouer', False, (255,255,255))
 
            if self.button_1.collidepoint ((self.mx, self.my)) and self.click == True :
                self.menu = False

            pygame.draw.rect(screen, (0, 0, 0), button_1)
            self.screen.blit(text1, (583, 255))
 
            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
 
    def draw_text(self, screen):
        screen.blit(self.textobj, self.textrect)
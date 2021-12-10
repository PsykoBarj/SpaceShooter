import pygame



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
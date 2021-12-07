import math
import random

import pygame
from pygame import mixer

# Initialisation du jeu
pygame.init()

# Creation de l'ecran de jeu
screen = pygame.display.set_mode((800, 600))

# Titre de l'ecran de jeu
pygame.display.set_caption("Space Shooter")

# Affichage du fond d'ecran du jeu
background = pygame.image.load('.\Images\Background.jpg')

# Son d'ambiance du jeu
mixer.music.load(".\sons\BackgroundMusic.mp3")
mixer.music.play(-1)

# Initialisation du joueur
playerImg = pygame.image.load('.\Images\Spaceship.png')
playerX = 500
playerY = 700
playerX_change = 0
playerY_change = 0

#Initialisation des ennemis
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3



for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('.\Images\enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(30)

# Prete -> La balle est dans le chargeur donc invisible a l'ecran
# Feu -> La balle est envoye et donc visible a l'ecran

bulletImg = pygame.image.load('.\Images\Bullet.png')
bulletX = playerX
bulletY = playerY
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# Bruitage des balles
SHOOT_SOUND = pygame.mixer.Sound('./Sons/shoot.wav')
SHOOT_SOUND.set_volume(0.5)

# Affichage du score , initialiser a 0 et en police freesansbold de taille 32
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
# Position du score
textX = 10
testY = 10

# Texte du Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Fonction de l'affichage du score
def show_score(x, y):
    # Rendu de l'affichage, on cherche si il y a un score et on l'affiche en blanc
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    # Permet d'afficher le score sur l'ecran de jeu
    screen.blit(score, (x, y))

# Affichage de fin de jeu en cas de perte de la partie
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Fonction pour afficher le joueur sur l'ecran de jeu
def player(x, y):
    screen.blit(playerImg, (x, y))

pygame.key.set_repeat(400,30)
# Fonction pour afficher les ennemis a l'ecran (position et nombre)
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Fonction des balles du joueur lorsqu'elles sont tire
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))

# Fonction de collision entre les balles et les enemies
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Boucle principal du jeu
running = True
while running:

    screen.fill((0,0,0))
    # Fond du jeu
    screen.blit(background, (0, 0))
    speed = 1
    # Indique que si l'on clique sur la croix le jeu s'eteint en coupant la boucle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Controle du vaisseau joueur
        if event.type == pygame.KEYDOWN:
        # Appui sur la fleche de gauche
            if event.key == pygame.K_LEFT:
                playerX_change = -speed
        # Appui sur la fleche de droite
            elif event.key == pygame.K_RIGHT:
                playerX_change = speed
        # Appui sur la fleche du haut
            elif event.key == pygame.K_UP:
                playerY_change = -speed
        # Appui sur la fleche du bas
            elif event.key == pygame.K_DOWN:
                playerY_change = speed
            elif event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0
        # Appui sur la touche espace pour tirer
           
            
    # Ces deux blocs empechent le vaisseau de sortir du cadre
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 530:
        playerY = 530

     # Indique que si l'ennemi passe en bas de l'ecran alors la partie est perdue et affiche Game Over
    for i in range(num_of_enemies):
        if enemyY[i]>450:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        # Deplacement de l'ennemi, lorsqu'il arrive tout a gauche descend de 1 pixel et a droite pareil
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Lors d'une collision la balle est reinitialiser et l'ennemi respawn aleatoirement en haut de l'ecran
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Fait disparaitre la balle a -20pixels hors du cadre
    if bulletY <= -20:
        bulletY = playerY
        bullet_state = "ready"

    # Mise en mouvement de la balle et son lors du tir
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        SHOOT_SOUND.play()

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
    

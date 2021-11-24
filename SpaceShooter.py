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
playerX = 200
playerY = 200
playerX_change = 0

#Initialisation des ennemis
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('.\Images\Spaceship.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Prete -> La balle est dans le chargeur donc invisible a l'ecran
# Feu -> La balle est envoye et donc visible a l'ecran

bulletImg = pygame.image.load('.\Images\Bullets.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "prete"

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

# Fonction pour afficher le joueur sur l'ecran de jeu
def player(x, y):
    screen.blit(playerImg, (x, y))

# Fonction pour afficher les ennemis a l'ecran (position et nombre)
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Fonction des balles du joueur lorsqu'elles sont tire
def fire_bullet(x, y):
    global bullet_state
    bubullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Fonction de collision entre les balles et les enemies
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

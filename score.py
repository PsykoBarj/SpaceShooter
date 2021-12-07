import pygame

class show_score:
        # Rendu de l'affichage, on cherche si il y a un score et on l'affiche en blanc
        score = font.render("Score : " + str(score_value), True, (255,255,255))
        # Permet d'afficher le score sur l'ecran de jeu
        screen.blit(score, (x, y))
import pygame
import random
import sys
import time
from pygame.locals import *

# Définir les variables de couleur
black_colour = pygame.Color(0, 0, 0)
white_colour = pygame.Color(255, 255, 255)
red_colour = pygame.Color(255, 0, 0)
grey_colour = pygame.Color(150, 150, 150)

# Définir la fonction de fin de jeu
def GameOver(gameSurface, score):
    # la police
    GameOver_font = pygame.font.SysFont("MicrosoftYaHei", 40)
    GameOver_colour = GameOver_font.render('Game Over', True, white_colour)
    # Définir l'emplacement du rappel
    GameOver_location = GameOver_colour.get_rect()
    GameOver_location.midtop = (320, 125)
    gameSurface.blit(GameOver_colour, GameOver_location)
    # Score
    score_font = pygame.font.SysFont("MicrosoftYaHei", 30)
    score_surf = score_font.render('SCORE: ' + str(score), True, red_colour)
    score_location = score_surf.get_rect()
    score_location.midtop = (320, 225)
    gameSurface.blit(score_surf, score_location)
    # Rafraîchir la page d'affichage
    pygame.display.flip()
    # Arrêt automatique après 5 secondes de sommeil
    time.sleep(5)
    # Quitter le jeu
    pygame.quit()
    # Quitter le programme
    sys.exit()


def main():
    # Initialiser pygame
    pygame.init()
    pygame.time.Clock()
    ftpsClock = pygame.time.Clock()
    # Créer une fenêtre
    gameSurface = pygame.display.set_mode((640, 480))
    # Définir le titre de la fenêtre
    pygame.display.set_caption('Serpent gourmand')
    # Initialiser la position de départ du serpent
    snakePosition = [100, 100]
    # Initialiser la longueur du serpent
    snakeLength = [[100, 100], [80, 100], [60, 100], [40, 100]]
    # Initialiser la position du bloc cible
    square_position = [300, 300]
    # Initialisez un nombre pour déterminer si le bloc cible existe
    square_nb = 1
    # Initialiser la direction, utilisée pour déplacer le serpent
    direction = "right"
    change_direction = direction
    score = 0

    # Effectuer la boucle de jeu principale
    while True:
        # Bouton de détection
        for event in pygame.event.get():
            if event.type == QUIT:
                # quitter le programme
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # Déterminer la touche enfoncée,
                # utilisez w, s, a, d pour indiquer le haut, le bas,
                # la gauche et la droite
                if event.key == K_RIGHT or event.key == ord('d'):
                    change_direction = "right"
                if event.key == K_LEFT or event.key == ord('a'):
                    change_direction = "left"
                if event.key == K_UP or event.key == ord('w'):
                    change_direction = "up"
                if event.key == K_DOWN or event.key == ord('s'):
                    change_direction = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # Déterminer si la direction du mouvement est opposée.
        # Parce que le serpent ne peut pas se déplacer dans la
        # direction opposée à la direction actuelle
        if change_direction == 'left' and not direction == 'right':
            direction = change_direction
        if change_direction == 'right' and not direction == 'left':
            direction = change_direction
        if change_direction == 'up' and not direction == 'down':
            direction = change_direction
        if change_direction == 'down' and not direction == 'up':
            direction = change_direction

        # Selon la direction, changer les coordonnées
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        # Augmenter la longueur du serpent
        snakeLength.insert(0, list(snakePosition))

        # Déterminer s'il faut manger le bloc cible
        if snakePosition[0] == square_position[0] and snakePosition[1] == square_position[1]:
            square_nb = 0
        else:
            snakeLength.pop()

        # Régénérer le bloc cible
        if square_nb == 0:
            # Déterminer une nouvelle position du bloc cible.
            # Générer aléatoirement x, y, développer vingt fois, dans la fenêtre
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            square_position = [int(x * 20), int(y * 20)]
            square_nb = 1
            score += 1
        # Dessiner un calque d'affichage pygame
        gameSurface.fill(black_colour)
        for position in snakeLength[1:]:
            # Le corps du serpent est blanc
            pygame.draw.rect(gameSurface, white_colour, Rect(position[0], position[1], 20, 20))
            # La tête de serpent est grise
            pygame.draw.rect(gameSurface, grey_colour, Rect(snakePosition[0], snakePosition[1], 20, 20))
            # Le carré cible est rouge
            pygame.draw.rect(gameSurface, red_colour, Rect(square_position[0], square_position[1], 20, 20))

        # Actualiser la couche d'affichage du pygame
        pygame.display.flip()

        # Déterminer si le serpent est mort
        if snakePosition[0] < 0 or snakePosition[0] > 620:
            GameOver(gameSurface, score)
        if snakePosition[1] < 0 or snakePosition[1] > 460:
            GameOver(gameSurface, score)
        for snakeBody in snakeLength[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                GameOver(gameSurface, score)

        # Contrôler la vitesse du jeu. Plus le corps du serpent est long,
        # plus la vitesse est rapide, jusqu'à ce qu'il atteigne une limite 40
        if len(snakeLength) < 40:
            speed = 6 + len(snakeLength) // 4
        else:
            speed = 16
        ftpsClock.tick(speed)


if __name__ == "__main__":
    main()
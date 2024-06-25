import pygame
pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 60
TITLE = "Platformer"
AUTHOR = "Manomay Tyagi"

#images clipping images from sprite sheet

#player 17x23

player = pygame.image.load('assets/characters.png')

# Set color key
player.set_colorkey((255, 255, 255))

# Set the clip area
player = player.subsurface(pygame.Rect(0, 0, 17, 23))

# Scale the surface
player = pygame.transform.scale(player, (17 * 2, 23 * 2))

#enemy 18x23


enemy = pygame.image.load('assets/characters.png')

# Set color key
enemy.set_colorkey((255, 255, 255))

# Set the clip area
enemy = enemy.subsurface(pygame.Rect(17, 0, 18, 23))

# Scale the surface
enemy = pygame.transform.scale(enemy, (17 * 2, 23 * 2))

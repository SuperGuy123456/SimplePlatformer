import pygame
pygame.init()
WINDOW_WIDTH = 630
WINDOW_HEIGHT = 480
FPS = 60
TITLE = "Platformer"
AUTHOR = "Manomay Tyagi"

#testmap

map = [
 , , , , , , , , , , , , , , , , , , , , ,
 , , , , , , , , , , , , , , , , , , , , ,
 , , , , , , , , , , , , , , , , , , , , ,
 , , , , , , , , , , , , , , , , , , , , ,
 , , , , , , , , , , , , , , , , , , , , ,
 , , , , , , , , , , , , , , , , , , , , ,
]

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

#confectionary items 

#normal sign 13x14

sign = pygame.image.load('assets/earth.png')
sign.set_colorkey((255, 255, 255))
sign = sign.subsurface(pygame.Rect(0, 0, 13, 14))
sign = pygame.transform.scale(sign, (13 * 2, 14 * 2))

#Ground 15x15

#Flat grass
flatgrass = pygame.image.load('assets/earth.png')
flatgrass.set_colorkey((255, 255, 255))
flatgrass = flatgrass.subsurface(pygame.Rect(13, 0, 15, 15))
flatgrass = pygame.transform.scale(flatgrass, (15 * 2, 15 * 2))
#under flatgrass

#flatgrassleft

#flatgrassright

#side wallleft

#side Wall right

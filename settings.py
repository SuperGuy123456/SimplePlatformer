import pygame
pygame.init()
WINDOW_WIDTH = 630
WINDOW_HEIGHT = 480
FPS = 60
TITLE = "Platformer"
AUTHOR = "Manomay Tyagi"

#testmap

map = [
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,
5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,
7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,
7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,
7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,
7,0,0,0,0,0,0,0,0,0,4,5,0,0,0,4,1,1,1,1,3,
7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,3,3,3,3,3,
7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,3,3,3,3,3,
3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,
2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,
3,3,2,3,3,3,3,3,3,2,3,3,3,2,3,3,3,3,3,3,3
]

#images clipping images from sprite sheet

#sky1

sky = pygame.image.load('assets/pinetreedark.png')
sky = pygame.transform.scale(sky, (WINDOW_WIDTH, WINDOW_HEIGHT))
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

#Flat grass 1
flatgrass = pygame.image.load('assets/earth.png')
flatgrass.set_colorkey((255, 255, 255))
flatgrass = flatgrass.subsurface(pygame.Rect(13, 0, 15, 15))
flatgrass = pygame.transform.scale(flatgrass, (15 * 2, 15 * 2))
#under flatgrass 2
under1 = pygame.image.load('assets/earth.png')
under1.set_colorkey((255, 255, 255))
under1 = under1.subsurface(pygame.Rect(28, 0, 15, 15))
under1 = pygame.transform.scale(under1, (15 * 2, 15 * 2))
#underflatgrass_other 3
under2 = pygame.image.load('assets/earth.png')
under2.set_colorkey((255, 255, 255))
under2 = under2.subsurface(pygame.Rect(15, 30, 15, 15))
under2 = pygame.transform.scale(under2, (15 * 2, 15 * 2))
#flatgrassleft 4
fgrassleft = pygame.image.load('assets/earth.png')
fgrassleft.set_colorkey((255, 255, 255))
fgrassleft = fgrassleft.subsurface(pygame.Rect(0, 15, 15, 15))
fgrassleft = pygame.transform.scale(fgrassleft, (15 * 2, 15 * 2))
#flatgrassright 5
fgrassright = pygame.image.load('assets/earth.png')
fgrassright.set_colorkey((255, 255, 255))
fgrassright = fgrassright.subsurface(pygame.Rect(15, 15, 15, 15))
fgrassright = pygame.transform.scale(fgrassright, (15 * 2, 15 * 2))
#side wallleft 6
swallleft = pygame.image.load('assets/earth.png')
swallleft.set_colorkey((255, 255, 255))
swallleft = swallleft.subsurface(pygame.Rect(30, 15, 15, 15))
swallleft = pygame.transform.scale(swallleft, (15 * 2, 15 * 2))
#side Wall right 7
swallright = pygame.image.load('assets/earth.png')
swallright.set_colorkey((255, 255, 255))
swallright = swallright.subsurface(pygame.Rect(0, 30, 15, 15))
swallright = pygame.transform.scale(swallright, (15 * 2, 15 * 2))

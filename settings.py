import pygame
pygame.init()
WINDOW_WIDTH = 630
WINDOW_HEIGHT = 480
FPS = 60
TITLE = "Platformer"
AUTHOR = "Manomay Tyagi"

#testmap

map = [
0,0,0,0,0,32,33,34,16,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,7,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,
8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,
13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,
13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,
13,0,0,0,0,0,0,0,0,0,21,22,0,0,0,22,28,26,28,20,9,
13,0,14,0,0,0,0,0,0,0,7,8,0,0,0,7,1,1,1,1,3,
13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,3,3,3,3,3,
13,21,31,27,31,21,21,25,28,27,27,21,19,31,21,9,3,3,3,3,3,
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

#items 15x15

#coin 15x15 32

coin = pygame.image.load('assets/items.png')
coin.set_colorkey((255, 255, 255))
coin = coin.subsurface(pygame.Rect(0, 0, 15, 15))
coin = pygame.transform.scale(coin, (15 * 2, 15 * 2))

#stampotion 15x15 33

stampotion = pygame.image.load('assets/items.png')
stampotion.set_colorkey((255, 255, 255))
stampotion = stampotion.subsurface(pygame.Rect(15, 0, 15, 15))
stampotion = pygame.transform.scale(stampotion, (15 * 2, 15 * 2))

#healthpotion 15x15 34

healthpotion = pygame.image.load('assets/items.png')
healthpotion.set_colorkey((255, 255, 255))
healthpotion = healthpotion.subsurface(pygame.Rect(30, 0, 15, 15))
healthpotion = pygame.transform.scale(healthpotion, (15 * 2, 15 * 2))

#strengthpotion 15x15 16

strengthpotion = pygame.image.load('assets/items.png')
strengthpotion.set_colorkey((255, 255, 255))
strengthpotion = strengthpotion.subsurface(pygame.Rect(0, 15, 15, 15))
strengthpotion = pygame.transform.scale(strengthpotion, (15 * 2, 15 * 2))

#confectionary items 

#normal sign 15x15 19

sign = pygame.image.load('assets/decor.png')
sign.set_colorkey((255, 255, 255))
sign = sign.subsurface(pygame.Rect(0, 0, 15, 15))
sign = pygame.transform.scale(sign, (15 * 2, 15 * 2))

#crate 15x15 20

crate = pygame.image.load('assets/decor.png')
crate.set_colorkey((255, 255, 255))
crate = crate.subsurface(pygame.Rect(15, 0, 15, 15))
crate = pygame.transform.scale(crate, (15 * 2, 15 * 2))

#little grass 15x15 21

grass = pygame.image.load('assets/decor.png')
grass.set_colorkey((255, 255, 255))
grass = grass.subsurface(pygame.Rect(30, 0, 15, 15))
grass = pygame.transform.scale(grass, (15 * 2, 15 * 2))

#daisy1 15x15 22

daisy = pygame.image.load('assets/decor.png')
daisy.set_colorkey((255, 255, 255))
daisy = daisy.subsurface(pygame.Rect(45, 0, 15, 15))
daisy = pygame.transform.scale(daisy, (15 * 2, 15 * 2))

#daisy2 15x15 27

daisy2 = pygame.image.load('assets/decor.png')
daisy2.set_colorkey((255, 255, 255))
daisy2 = daisy2.subsurface(pygame.Rect(30, 15, 15, 15))
daisy2 = pygame.transform.scale(daisy2, (15 * 2, 15 * 2))

#orangeflower1 15x15 28
orangeflower1 = pygame.image.load('assets/decor.png')
orangeflower1.set_colorkey((255, 255, 255))
orangeflower1 = orangeflower1.subsurface(pygame.Rect(45, 15, 15, 15))
orangeflower1 = pygame.transform.scale(orangeflower1, (15 * 2, 15 * 2))

#orangeflower2 15x15 31
orangeflower2 = pygame.image.load('assets/decor.png')
orangeflower2.set_colorkey((255, 255, 255))
orangeflower2 = orangeflower2.subsurface(pygame.Rect(0, 30, 15, 15))
orangeflower2 = pygame.transform.scale(orangeflower2, (15 * 2, 15 * 2))

#rock1 15x15 26

rock1 = pygame.image.load('assets/decor.png')
rock1.set_colorkey((255, 255, 255))
rock1 = rock1.subsurface(pygame.Rect(15, 15, 15, 15))
rock1 = pygame.transform.scale(rock1, (15 * 2, 15 * 2))

#rock2 15x15 25

rock2 = pygame.image.load('assets/decor.png')
rock2.set_colorkey((255, 255, 255))
rock2 = rock2.subsurface(pygame.Rect(0, 15, 15, 15))
rock2 = pygame.transform.scale(rock2, (15 * 2, 15 * 2))

#Ground 15x15

#Flat grass 1
flatgrass = pygame.image.load('assets/earth.png')
flatgrass.set_colorkey((255, 255, 255))
flatgrass = flatgrass.subsurface(pygame.Rect(13, 0, 15, 15))
flatgrass = pygame.transform.scale(flatgrass, (15 * 2, 15 * 2))
#under flatgrass 3
under1 = pygame.image.load('assets/earth.png')
under1.set_colorkey((255, 255, 255))
under1 = under1.subsurface(pygame.Rect(28, 0, 15, 15))
under1 = pygame.transform.scale(under1, (15 * 2, 15 * 2))
#underflatgrass_other 2
under2 = pygame.image.load('assets/earth.png')
under2.set_colorkey((255, 255, 255))
under2 = under2.subsurface(pygame.Rect(15, 30, 15, 15))
under2 = pygame.transform.scale(under2, (15 * 2, 15 * 2))
#flatgrassleft 7
fgrassleft = pygame.image.load('assets/earth.png')
fgrassleft.set_colorkey((255, 255, 255))
fgrassleft = fgrassleft.subsurface(pygame.Rect(0, 15, 15, 15))
fgrassleft = pygame.transform.scale(fgrassleft, (15 * 2, 15 * 2))
#flatgrassright 8
fgrassright = pygame.image.load('assets/earth.png')
fgrassright.set_colorkey((255, 255, 255))
fgrassright = fgrassright.subsurface(pygame.Rect(15, 15, 15, 15))
fgrassright = pygame.transform.scale(fgrassright, (15 * 2, 15 * 2))
#side wallleft 9
swallleft = pygame.image.load('assets/earth.png')
swallleft.set_colorkey((255, 255, 255))
swallleft = swallleft.subsurface(pygame.Rect(30, 15, 15, 15))
swallleft = pygame.transform.scale(swallleft, (15 * 2, 15 * 2))
#side Wall right 13
swallright = pygame.image.load('assets/earth.png')
swallright.set_colorkey((255, 255, 255))
swallright = swallright.subsurface(pygame.Rect(0, 30, 15, 15))
swallright = pygame.transform.scale(swallright, (15 * 2, 15 * 2))

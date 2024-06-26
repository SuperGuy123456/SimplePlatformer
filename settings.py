import pygame
pygame.init()
WINDOW_WIDTH = 630
WINDOW_HEIGHT = 480
FPS = 60
TITLE = "Platformer"
AUTHOR = "Manomay Tyagi"

#testmap
width = 49
TILE_SIZE = 30


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

#checkpoint 15x15

checkpoint = pygame.image.load('assets/decor.png')
checkpoint.set_colorkey((255, 255, 255))
checkpoint = checkpoint.subsurface(pygame.Rect(15, 30, 15, 15))
checkpoint = pygame.transform.scale(checkpoint, (15 * 2, 15 * 2))

#active_checkpoint 15x15

active_checkpoint = pygame.image.load('assets/decor.png')
active_checkpoint.set_colorkey((255, 255, 255))
active_checkpoint = active_checkpoint.subsurface(pygame.Rect(30, 30, 15, 15))
active_checkpoint = pygame.transform.scale(active_checkpoint, (15 * 2, 15 * 2))

#enemy 18x23


enemy = pygame.image.load('assets/characters.png')

# Set color key
enemy.set_colorkey((255, 255, 255))

# Set the clip area
enemy = enemy.subsurface(pygame.Rect(17, 0, 18, 23))

# Scale the surface
enemy = pygame.transform.scale(enemy, (17 * 2, 23 * 2))

#trader 18x23
trader_types = ["Common Trader","Rare Trader","Epic Trader"]

trader = pygame.image.load('assets/characters.png')
trader.set_colorkey((255, 255, 255))
trader = trader.subsurface(pygame.Rect(35, 0, 18, 23))
trader = pygame.transform.scale(trader, (18 * 2, 23 * 2))

# ... 11x6
interact = pygame.image.load('assets/effects.png')
interact.set_colorkey((255, 255, 255))
interact = interact.subsurface(pygame.Rect(0, 0, 11, 6))
interact = pygame.transform.scale(interact, (11 * 2, 6 * 2))

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

#jumppotion 15x15

jumppotion = pygame.image.load('assets/items.png') 
jumppotion.set_colorkey((255, 255, 255))
jumppotion = jumppotion.subsurface(pygame.Rect(15, 15, 15, 15))
jumppotion = pygame.transform.scale(jumppotion, (15 * 2, 15 * 2))

#invispotion 15x15

invispotion = pygame.image.load('assets/items.png')
invispotion.set_colorkey((255, 255, 255))
invispotion = invispotion.subsurface(pygame.Rect(30, 15, 15, 15))
invispotion = pygame.transform.scale(invispotion, (15 * 2, 15 * 2))

#permstampotion 15x15

permstampotion = pygame.image.load('assets/items.png')
permstampotion.set_colorkey((255, 255, 255))
permstampotion = permstampotion.subsurface(pygame.Rect(45, 0, 15, 15))
permstampotion = pygame.transform.scale(permstampotion, (15 * 2, 15 * 2))

#permjumppotion 15x15

permjumppotion = pygame.image.load('assets/items.png')
permjumppotion.set_colorkey((255, 255, 255))
permjumppotion = permjumppotion.subsurface(pygame.Rect(45, 15, 15, 15))
permjumppotion = pygame.transform.scale(permjumppotion, (15 * 2, 15 * 2))

#confectionary items 

#normal sign 15x15 19

sign = pygame.image.load('assets/decor.png')
sign.set_colorkey((255, 255, 255))
sign = sign.subsurface(pygame.Rect(0, 0, 15, 15))
sign = pygame.transform.scale(sign, (15 * 2, 15 * 2))

#crate 15x15 20 ------Animation object ---------

crate = pygame.image.load('assets/decor.png')
crate.set_colorkey((255, 255, 255))
crate = crate.subsurface(pygame.Rect(15, 0, 15, 15))
crate = pygame.transform.scale(crate, (15 * 2, 15 * 2))

#cratef1 12x12

cratef1 = pygame.image.load('assets/effects.png')
cratef1.set_colorkey((255, 255, 255))
cratef1 = cratef1.subsurface(pygame.Rect(0, 11, 12, 12))
cratef1 = pygame.transform.scale(cratef1, (12 * 2, 12 * 2))

#cratef2 14x12

cratef2 = pygame.image.load('assets/effects.png')
cratef2.set_colorkey((255, 255, 255))
cratef2 = cratef2.subsurface(pygame.Rect(13, 11, 14, 12))
cratef2 = pygame.transform.scale(cratef2, (14 * 2, 12 * 2))

#cratef3 14x11

cratef3 = pygame.image.load('assets/effects.png')
cratef3.set_colorkey((255, 255, 255))
cratef3 = cratef3.subsurface(pygame.Rect(29, 11, 14, 12))
cratef3 = pygame.transform.scale(cratef3, (14 * 2, 12 * 2))

#cratef4 15x12 44

cratef4 = pygame.image.load('assets/effects.png')
cratef4.set_colorkey((255, 255, 255))
cratef4 = cratef4.subsurface(pygame.Rect(44, 11, 15, 12))
cratef4 = pygame.transform.scale(cratef4, (15 * 2, 12 * 2))
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

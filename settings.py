import pygame
pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 60
TITLE = "Platformer"
AUTHOR = "Manomay Tyagi"

#images

#player 17x23

player = pygame.image.load('assets/characters.png') 
player = player.set_colorkey((255,255,255))
player = pygame.Surface.set_clip(player,(0,0,17,23))
player = pygame.transform.scale(player,(17*2,23*2))

#enemy 18x23
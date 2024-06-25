import pygame
import settings
from player import Player
from ground import Ground
from enemy import Enemy
from specialitems import item

pygame.init()
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

run = True
clock = pygame.time.Clock()

ground = Ground(0, 400, "normalground",(settings.WINDOW_WIDTH, 100), 0.5)
ground2 = Ground(300, 300, "normalground",(settings.WINDOW_WIDTH, 100), 0.5)
grounds = [ground,ground2]

player = Player(100,100)
player.set_ground(grounds)

enemy = Enemy(200,200)

enemy.set_ground(grounds)

flatgrass = item(0,0,settings.flatgrass)
under1 = item(30,0,settings.under1)
under2 = item(60,0,settings.under2)
fgrassleft = item(0,30,settings.fgrassleft)
fgrassright = item(30,30,settings.fgrassright)
sidewallleft = item(0,60,settings.swallleft)
sidewallright = item(30,60,settings.swallright)

items = [flatgrass,under1,under2,fgrassleft,fgrassright,sidewallleft,sidewallright]
while run:
    clock.tick(settings.FPS)
    screen.fill((0,0,0))
    player.draw(screen)
    enemy.draw(screen)
    for i in grounds:
        i.draw(screen)

    for i in items:
        i.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
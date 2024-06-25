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

grounds = []
groupedrects = []
tile_size = 30
map_width = 21
map_height = 16


# Ensure the map size is correct
if len(settings.map) != map_width * map_height:
    raise ValueError(f"Map should have {map_width * map_height} elements")

for index, thing in enumerate(settings.map):
    x = (index % map_width) * tile_size
    y = (index // map_width) * tile_size
    if thing == 0:
        continue
    elif thing == 1:
        grounds.append(Ground(x, y, settings.flatgrass, 1.0))
    elif thing == 2:
        grounds.append(Ground(x, y, settings.under1, 1.0))
    elif thing == 3:
        grounds.append(Ground(x, y, settings.under2, 1.0))
    elif thing == 4:
        grounds.append(Ground(x, y, settings.fgrassleft, 1.0))
    elif thing == 5:
        grounds.append(Ground(x, y, settings.fgrassright, 1.0))
    elif thing == 6:
        grounds.append(Ground(x, y, settings.swallleft, 1.0))
    elif thing == 7:
        grounds.append(Ground(x, y, settings.swallright, 1.0))


player = Player(100, 100)
player.set_ground(grounds)

enemy = Enemy(200, 200)
enemy.set_ground(grounds)

flatgrass = item(0, 0, settings.flatgrass)
under1 = item(30, 0, settings.under1)
under2 = item(60, 0, settings.under2)
fgrassleft = item(0, 30, settings.fgrassleft)
fgrassright = item(30, 30, settings.fgrassright)
sidewallleft = item(0, 60, settings.swallleft)
sidewallright = item(30, 60, settings.swallright)

items = [flatgrass, under1, under2, fgrassleft, fgrassright, sidewallleft, sidewallright]
hitboxes = False
while run:
    clock.tick(settings.FPS)
    screen.fill((0, 0, 0))
    screen.blit(settings.sky, (0, 0))
    player.draw(screen)
    enemy.draw(screen)
    if hitboxes:
        pygame.draw.rect(screen, (255, 255, 255), player.rect, 1)
        pygame.draw.rect(screen, (255, 255, 255), enemy.rect, 1)
    for ground in grounds:
        ground.draw(screen)
        if hitboxes:
            pygame.draw.rect(screen, (255, 255, 255), ground.rect, 1)

    for item in items:
        item.draw(screen)
        if hitboxes:
            pygame.draw.rect(screen, (255, 255, 255), item.rect, 1)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_h:
                if hitboxes:
                    hitboxes = False
                else:
                    hitboxes = True

pygame.quit()

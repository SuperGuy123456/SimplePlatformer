import pygame
import settings
from player import Player
from ground import Ground
from enemy import Enemy
from specialitems import decor
from item import Item
from flatimg import Flat

pygame.init()
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

run = True
clock = pygame.time.Clock()

grounds = []
enemies = []
items = []
flats = []
tile_size = 30
map_width = 21
map_height = 16
decors = []
player = Player(100,100)
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
        flats.append(Flat(x, y, settings.under1))
    elif thing == 3:
        flats.append(Flat(x, y, settings.under2))
    elif thing == 7:
        grounds.append(Ground(x, y, settings.fgrassleft, 1.0))
    elif thing == 8:
        grounds.append(Ground(x, y, settings.fgrassright, 1.0))
    elif thing == 9:
        grounds.append(Ground(x, y, settings.swallleft, 1.0))
    elif thing == 13:
        grounds.append(Ground(x, y, settings.swallright, 1.0))
    elif thing == 19:
        decors.append(decor(x, y, settings.sign,True,(x+15,y + 30)))
    elif thing == 20:
        decors.append(decor(x,y,settings.crate,True,(x+15,y + 30)))
    elif thing == 21:
        flats.append(Flat(x,y,settings.grass))
    elif thing == 22:
        flats.append(Flat(x,y,settings.daisy))
    elif thing == 27:
        flats.append(Flat(x,y,settings.daisy2))
    elif thing == 28:
        flats.append(Flat(x,y,settings.orangeflower1))
    elif thing == 31:
        flats.append(Flat(x,y,settings.orangeflower2))
    elif thing == 26:
        flats.append(Flat(x,y,settings.rock1))
    elif thing == 25:
        flats.append(Flat(x,y,settings.rock2))

    elif thing == 14:
        player = Player(x,y)
    elif thing == 15:
        enemies.append(Enemy(x,y,settings.enemy, 100,1))

    elif thing == 32:
        items.append(Item(x,y,settings.coin,"coin"))
    elif thing == 33:
        items.append(Item(x,y,settings.stampotion,"speed"))
    elif thing == 34:
        items.append(Item(x,y,settings.healthpotion,"health"))
    elif thing == 16:
        items.append(Item(x,y,settings.strengthpotion,"strength"))
    




player.set_enemies(enemies)
player.set_ground(grounds)
player.set_items(items)
player.set_decors(decors)

for enemy in enemies:
    enemy.set_player(player)
    enemy.set_ground(grounds)

for item in items:
    item.set_ground(grounds)

hitboxes = False

while run:
    clock.tick(settings.FPS)
    screen.fill((0, 0, 0))
    screen.blit(settings.sky, (0, 0))
    items = player.items
    for flat in flats:
        flat.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
        if hitboxes:
            pygame.draw.rect(screen, (255, 255, 255), enemy.rect, 1)
            pygame.draw.circle(screen,(150,150,150),enemy.rect.center,enemy.view,1)
    for item in items:
        item.draw(screen)
        if hitboxes:
            pygame.draw.rect(screen, (255, 255, 255), item.rect, 1)
    if hitboxes:
        pygame.draw.rect(screen, (255, 255, 255), player.rect, 1)
        pygame.draw.rect(screen, (255, 255, 255), player.attack_rect, 1)
        
    for ground in grounds:
        ground.draw(screen)
        if hitboxes:
            pygame.draw.rect(screen, (255, 255, 255), ground.rect, 1)

    for decor in decors:
        decor.draw(screen)
        if hitboxes:
            if decor.makerect:
                pygame.draw.rect(screen, (255, 255, 255), decor.rect, 1)

 
    player.draw(screen)

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

        player.check_use(event)

pygame.quit()

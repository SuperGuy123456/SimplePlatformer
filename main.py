import pygame
import settings
from player import Player
from ground import Ground
from enemy import Enemy

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

while run:
    clock.tick(settings.FPS)
    screen.fill((0,0,0))
    player.draw(screen)
    enemy.draw(screen)
    for i in grounds:
        i.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
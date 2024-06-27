import pygame
import settings
from time import time
from random import choice
from item import Item
pygame.init()

class decor(pygame.sprite.Sprite):
    def __init__(self, x, y, image, rect = True, bottompos = None):
        super().__init__()
        self.image = image
        self.makerect = rect
        self.highlight = False
        if rect:
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.x = self.rect.x
            self.y = self.rect.y
            self.bottompos = bottompos
        
        else:
            self.x = x
            self.y = y
        self.anistarted = False
        self.gravity = 0.8
        if self.image == settings.crate:
            self.frames = [settings.cratef1, settings.cratef2, settings.cratef3, settings.cratef4]
            self.index = 0
            self.anistarted = False
            self.lasttime = time()
            self.done = False

    def draw(self,screen,camera):
        if self.anistarted == False:
            if self.makerect:
                screen.blit(self.image, camera.apply_position(self.rect))
            else:
                screen.blit(self.image, (self.x,self.y))
        else:
            screen.blit(self.frames[self.index], camera.apply_position(self.rect))
        if self.highlight:
            pygame.draw.rect(screen, (255, 255, 255),camera.apply_position( self.rect), 1)
        self.highlight = False
        self.update()

    def update(self):
        if self.image == settings.sign:
            pass #print("sign interaction")
        elif self.image == settings.crate:
            if self.anistarted:
                self.animate()
                self.apply_gravity()
                self.rect = self.frames[self.index].get_rect()
            else:
                self.rect = self.image.get_rect()
            self.rect.bottomleft = (self.bottompos[0]-15,self.bottompos[1])

    def animate(self):
        now = time()
        if now - self.lasttime > 0.1 and self.index < 3:
            self.lasttime = now
            self.index += 1
        if self.index == 3:
            self.done = True

    def apply_gravity(self):
            self.y += self.gravity
            if self.makerect:
                self.rect.y = self.y

    def crate(self, player):
        if self.done == False:
            self.player = player
            self.anistarted = True  
            choices = ["coin","speed","health","strength"]
            item = choice(choices)
            if item == "coin":
                player.inventory.add_item(Item(self.x, self.y, settings.coin, "coin"))
            if item == "speed":
                player.inventory.add_item(Item(self.x, self.y, settings.stampotion, "speed"))
            if item == "health":
                player.inventory.add_item(Item(self.x, self.y, settings.healthpotion, "health"))
            if item == "strength":
                player.inventory.add_item(Item(self.x, self.y, settings.strengthpotion, "strength"))

            for item in player.items:
                item.set_ground(player.grounds)

    def highlight_on(self):
        self.highlight = True

        
        
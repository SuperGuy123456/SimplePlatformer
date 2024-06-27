# item.py

import pygame
import settings
from time import time
from camera import Camera

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, image, Type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.accx = 0
        self.accy = 0
        self.grounded = False
        self.current_ground = None
        self.air_control_factor = 0.5  # Factor to reduce horizontal movement speed in the air
        self.type = Type
        self.highlight = False

    def update(self):
        self.rect.x += self.accx
        self.handle_horizontal_collisions()
        self.rect.y += self.accy
        self.handle_vertical_collisions()
        if not self.grounded:
            self.accy += 0.8

    def handle_horizontal_collisions(self):
        for ground in self.grounds:
            if self.rect.colliderect(ground.rect):
                if self.accx > 0:
                    self.rect.right = ground.rect.left
                elif self.accx < 0:
                    self.rect.left = ground.rect.right
                self.accx = 0

    def handle_vertical_collisions(self):
        self.grounded = False
        for ground in self.grounds:
            if self.rect.colliderect(ground.rect):
                if self.accy > 0:
                    self.rect.bottom = ground.rect.top
                    self.grounded = True
                    self.current_ground = ground
                elif self.accy < 0:
                    self.rect.top = ground.rect.bottom
                self.accy = 0
        if not self.grounded:
            self.current_ground = None

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply_position(self.rect))
        self.update()
        if self.highlight:
            pygame.draw.rect(screen, (255, 255, 255), camera.apply_position(self.rect), 1)
            self.highlight = False

    def set_ground(self, grounds):
        self.grounds = grounds

    def picked(self, player):
        if len(player.inventory.blits) < player.inventory.size:
            player.inventory.add_item(self)
            print(player.inventory)
        else:
            print("inventory full")

    def highlight_on(self):
        self.highlight = True

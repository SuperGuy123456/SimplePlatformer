import pygame
import settings
from time import time
pygame.init()

# The player class that is an image and a rectangle that inhibits platformer-style collision
class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, image,Type):
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
            
    def update(self):
        # Clamp horizontal speed

        # Update horizontal position
        self.rect.x += self.accx
        self.handle_horizontal_collisions()

        # Update vertical position
        self.rect.y += self.accy
        self.handle_vertical_collisions()
        

        # Apply gravity if not grounded
        if not self.grounded:
            self.accy += 0.8

        # Apply friction from the current ground if grounded
        if self.grounded and self.current_ground:
            friction = self.current_ground.friction
            if self.accx > 0:
                self.accx -= friction
                if self.accx < 0:
                    self.accx = 0
            elif self.accx < 0:
                self.accx += friction
                if self.accx > 0:
                    self.accx = 0
        

    def handle_horizontal_collisions(self):
        for ground in self.grounds:
            if self.rect.colliderect(ground):
                if self.accx > 0:  # Moving right
                    self.rect.right = ground.rect.left
                elif self.accx < 0:  # Moving left
                    self.rect.left = ground.rect.right
                self.accx = 0  # Stop horizontal movement on collision

    def handle_vertical_collisions(self):
        self.grounded = False  # Assume player is not grounded
        for ground in self.grounds:
            if self.rect.colliderect(ground):
                if self.accy > 0:  # Falling
                    self.rect.bottom = ground.rect.top
                    self.grounded = True
                    self.current_ground = ground
                elif self.accy < 0:  # Jumping
                    self.rect.top = ground.rect.bottom
                self.accy = 0  # Stop vertical movement on collision
        if not self.grounded:
            self.current_ground = None

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.update()

    def set_ground(self, grounds):
        self.grounds = grounds

    def picked(self,player):
        if len(player.inventory.blits) < player.inventory.size:
            player.inventory.add_item(self)
            print(player.inventory)
        else:
            print("inventory full")

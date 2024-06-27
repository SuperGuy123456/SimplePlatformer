# enemy.py

import pygame
from time import time
from random import randint
import settings
from item import Item
from camera import Camera

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, view, speed=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.accx = 0
        self.accy = 0
        self.grounded = False
        self.current_ground = None
        self.air_control_factor = 0.5  # Factor to reduce horizontal movement speed in the air
        self.max_speed = 3  # Maximum horizontal speed
        self.health = 10
        self.attackpow = 2
        self.canattack = True
        self.attack_cooldown = 2
        self.lasttime = 0
        self.player = None
        self.view = view
        self.jumpview = view  # in what proximity the enemy will try to jump to reach player
        self.highlight = False

    def set_player(self, player):
        self.player = player

    def movehorizontal(self, right):
        if right:
            self.accx += self.speed if self.grounded else self.speed * self.air_control_factor
        else:
            self.accx -= self.speed if self.grounded else self.speed * self.air_control_factor

    def movevertical(self):
        if self.grounded:
            self.accy = -15
            self.grounded = False
        self.rect.y += self.accy
        self.handle_vertical_collisions()

    def update(self):
        self.search_player()
        if self.accx > self.max_speed:
            self.accx = self.max_speed
        elif self.accx < -self.max_speed:
            self.accx = -self.max_speed
        self.rect.x += self.accx
        self.handle_horizontal_collisions()
        self.rect.y += self.accy
        self.handle_vertical_collisions()
        if not self.grounded:
            self.accy += 0.8
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

    def jump(self):
        if self.grounded:
            self.accy = -15  # Set initial jump velocity
            self.grounded = False

    def attack(self):
        if self.canattack:
            self.canattack = False
            self.lasttime = time()
            return True
        else:
            if time() - self.lasttime > self.attack_cooldown:
                self.canattack = True
                return True
            else:
                return False
        return False

    def search_player(self):
        player_x, player_y = self.player.rect.x, self.player.rect.y
        player_speed = self.player.speed

        if abs(self.rect.x - player_x) < self.view and abs(self.rect.y - player_y) < self.view and self.player.invisible == False:
            predicted_player_x = player_x + player_speed * 5
            predicted_player_y = player_y
            if self.rect.x < predicted_player_x:
                self.movehorizontal(True)
            elif self.rect.x > predicted_player_x:
                self.movehorizontal(False)
            if self.rect.bottom < predicted_player_y and abs(self.rect.y - predicted_player_y) < self.jumpview:
                self.jump()
                print("jumping")
            elif self.rect.y > player_y and abs(self.rect.y - player_y) < self.jumpview:
                self.jump()
                print("jumping")
            return True
        return False

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
        if self.health > 0:
            screen.blit(self.image, camera.apply_position(self.rect))
            if self.highlight:
                pygame.draw.rect(screen, (255, 255, 255), camera.apply_position(self.rect), 1)
                self.highlight = False
            self.update()
        else:
            for i in self.player.enemies:
                if i == self:
                    self.player.enemies.remove(i)
            for i in range(0, randint(1, 2)):
                self.player.inventory.add_item(Item(0, 0, settings.coin, "coin"))

    def set_ground(self, grounds):
        self.grounds = grounds

    def highlight_on(self):
        self.highlight = True

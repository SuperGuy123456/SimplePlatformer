import pygame
import settings
from inventory import Inventory
from time import time
from HUD import HUD
pygame.init()

# The player class that is an image and a rectangle that inhibits platformer-style collision
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = settings.player
        self.outline_rect = pygame.Rect(0, 0, 200 + 5, 25)
        self.leftimage = pygame.transform.flip(self.image, True, False)
        self.index = 0
        self.images = [self.image, self.leftimage]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.attack_rect = pygame.Rect(x, y, 60, 30)
        self.health_rect = pygame.Rect(5, 0, 200, 25)
        self.speed = 1
        self.accx = 0
        self.accy = 0
        self.grounded = False
        self.current_ground = None
        self.air_control_factor = 0.5  # Factor to reduce horizontal movement speed in the air
        self.max_speed = 5  # Maximum horizontal speed
        self.health = 100
        self.attackpow = 2
        self.attack_cooldown = 1
        self.lasttime = time()
        self.canattack = True
        self.direction = True  # right = True, left = False
        self.inventory = Inventory(5)
        self.active_effect = None
        self.effect_duration = 0
        self.base_health = 100
        self.base_attackpow = 2
        self.base_speed = 1
        self.base_max_speed = 5
        self.base_attack_cooldown = 1
        self.effect_start_time = 0
        self.coins = 0
        self.hud = HUD(self)

    def attack(self):
        if self.canattack:
            self.canattack = False
            self.lasttime = time()
            print("attacked")
            self.checkifhit()
        else:
            if time() - self.lasttime > self.attack_cooldown:
                self.canattack = True
                return 0
            else:
                return 0

    def checkifhit(self):
        for enemy in self.enemies:
            if self.attack_rect.colliderect(enemy.rect):
                enemy.health -= self.attackpow
                print("enemy health: ", enemy.health)
        items = []
        for item in self.items:
            if self.attack_rect.colliderect(item.rect):
                item.picked(self)
            else:
                items.append(item)
        self.items = items

        decors = []
        for decor in self.decors:
            try:
                if self.attack_rect.colliderect(decor.rect) and decor.image == settings.crate:
                    decor.crate(self)
                decors.append(decor)
            except:
                decors.append(decor)
        self.decors = decors

    def use(self):
        if self.active_effect:
            blank = False
            for i, (item, pos) in enumerate(self.inventory.blits):
                if i == self.inventory.heighlightindex:
                    if item.type == "coin":
                        blank = True

            if blank == False:
                self.attackpow = self.base_attackpow
                self.speed = self.base_speed
                self.max_speed = self.base_max_speed
                self.attack_cooldown = self.base_attack_cooldown
                self.active_effect = None
                self.effect_duration = 0
                self.use_item()
            else:
                self.use_item()
        else:
            self.use_item()

    def use_item(self):
        item_used = False
        for i, (item, pos) in enumerate(self.inventory.blits):
            if i == self.inventory.heighlightindex:
                if item.type == "health":
                    self.health += 20
                    self.active_effect = "health"
                    self.effect_duration = 10
                    self.effect_start_time = time()
                    item_used = True

                if item.type == "strength":
                    self.attackpow += 1
                    self.active_effect = "strength"
                    self.effect_duration = 10
                    self.effect_start_time = time()
                    item_used = True
                
                if item.type == "speed":
                    self.speed += 1
                    self.max_speed += 2
                    self.attack_cooldown -= 0.5
                    self.active_effect = "speed"
                    self.effect_duration = 10
                    self.effect_start_time = time()
                    item_used = True

                if item.type == "coin":
                    self.coins += 1
                    item_used = True

                if item_used:
                    # Remove the used item from the inventory
                    self.inventory.blits.pop(i)

                    # Adjust the inventory slots visually with y-coordinate set to 450
                    self.inventory.blits = [(item, (index * 30, 450)) for index, (item, pos) in enumerate(self.inventory.blits)]
                    self.inventory.imagex -= 30
                    self.inventory.set_inv(self.inventory.blits, self.inventory.imagex)

                    # Adjust the highlight index
                    self.inventory.heighlightindex = max(0, self.inventory.heighlightindex - 1)
                    break

    def highlight(self):
        for item in self.items:
            if self.attack_rect.colliderect(item.rect):
                item.highlight_on()
        
        for decor in self.decors:
            if self.attack_rect.colliderect(decor.rect):
                decor.highlight_on()

        for enemy in self.enemies:
            if self.attack_rect.colliderect(enemy.rect):
                enemy.highlight_on()


    def update(self):
        self.highlight()
        print(self.active_effect)
        self.health_rect = pygame.Rect(5, 0, self.health * 2, 25)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.accx -= self.speed if self.grounded else self.speed * self.air_control_factor
            self.direction = False
        if keys[pygame.K_RIGHT]:
            self.accx += self.speed if self.grounded else self.speed * self.air_control_factor
            self.direction = True
        if keys[pygame.K_UP] and self.grounded:
            self.accy -= 13
            self.grounded = False
        if keys[pygame.K_a]:
            self.attack()
        if keys[pygame.K_1]:
            self.inventory.select(0)
        if keys[pygame.K_2]:
            self.inventory.select(1)
        if keys[pygame.K_3]:
            self.inventory.select(2)
        if keys[pygame.K_4]:
            self.inventory.select(3)
        if keys[pygame.K_5]:
            self.inventory.select(4)
        # Clamp horizontal speed
        if self.accx > self.max_speed:
            self.accx = self.max_speed
        elif self.accx < -self.max_speed:
            self.accx = -self.max_speed

        # Update horizontal position
        self.rect.x += self.accx
        self.handle_horizontal_collisions()

        # Update vertical position
        self.rect.y += self.accy
        self.handle_vertical_collisions()
        if self.direction:
            self.attack_rect.left = self.rect.left
            self.attack_rect.y = self.rect.topright[1]
        else:
            self.attack_rect.right = self.rect.right
            self.attack_rect.y = self.rect.topleft[1]

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
        for enemy in self.enemies:
            if self.rect.colliderect(enemy):
                if enemy.attack():
                    self.health -= enemy.attackpow
        if self.health <= 0:
            print("ded")
            quit()

        if self.active_effect == "health":
            if time() - self.effect_start_time <= self.effect_duration:
                self.health += 5 * (1 / settings.FPS)
                if self.health > self.base_health:
                    self.health = self.base_health
            else:
                self.active_effect = None
        elif self.active_effect == "strength":
            if time() - self.effect_start_time <= self.effect_duration:
                pass
            else:
                self.active_effect = None
                self.attackpow = self.base_attackpow
        elif self.active_effect == "speed":
            if time() - self.effect_start_time <= self.effect_duration:
                pass
            else:
                self.active_effect = None
                self.speed = self.base_speed
                self.max_speed = self.base_max_speed
                self.attack_cooldown = self.base_attack_cooldown

    def check_use(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_e:
                self.use()

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
        if self.direction:
            surface.blit(self.images[0], self.rect)
        else:
            surface.blit(self.images[1], self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.health_rect)
        pygame.draw.rect(surface, (255, 255, 255), self.outline_rect, 5)
        self.inventory.draw(surface)
        self.hud.draw(surface)
        self.update()

    def set_ground(self, grounds):
        self.grounds = grounds

    def set_enemies(self, enemies):
        self.enemies = enemies

    def set_items(self, items):
        self.items = items

    def set_decors(self, decors):
        self.decors = decors

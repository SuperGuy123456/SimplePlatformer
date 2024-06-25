import pygame
import settings
from time import time
pygame.init()

# The player class that is an image and a rectangle that inhibits platformer-style collision
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = settings.player
        self.outline_rect = pygame.Rect(0,0,200+5,25)
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
        self.direction = True #right = True, left = False

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
    def update(self):
        self.health_rect = pygame.Rect(5, 0, self.health*2, 25)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.accx -= self.speed if self.grounded else self.speed * self.air_control_factor
            self.direction = False
        if keys[pygame.K_RIGHT]:
            self.accx += self.speed if self.grounded else self.speed * self.air_control_factor
            self.direction = True
        if keys[pygame.K_UP] and self.grounded:
            self.accy -= 15
            self.grounded = False
        if keys[pygame.K_a]:
            self.attack()
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
                    #print("lost health:", enemy.attackpow)
        if self.health <= 0:
            print("ded")
            quit()
        #print("health: ", self.health)

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
        pygame.draw.rect(surface, (255, 0, 0), self.health_rect)
        pygame.draw.rect(surface, (255, 255, 255), self.outline_rect,5)
        self.update()

    def set_ground(self, grounds):
        self.grounds = grounds

    def set_enemies(self, enemies):
        self.enemies = enemies

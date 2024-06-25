import pygame
import settings
pygame.init()

# The player class that is an image and a rectangle that inhibits platformer-style collision
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y,image, player, view, speed = 1):
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

        self.player = player
        self.view = view
        self.jumpview = view #in what proximity the enemy will try to jump to reach player


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

    def search_player(self):
        if abs(self.rect.x - self.player.rect.x) < self.view and abs(self.rect.y - self.player.rect.y) < self.view:
            direction = self.rect.x - self.player.rect.x
            if direction > 0:
                self.movehorizontal(False)
            else:
                self.movehorizontal(True)
            if self.rect.bottom < self.player.rect.bottom and abs(self.rect.y - self.player.rect.y) < self.jumpview:
                self.movevertical()
                print("jumping")
            return True
        return False

    def handle_horizontal_collisions(self):
        for ground in self.grounds:
            if self.rect.colliderect(ground.rect):
                if self.accx > 0:  # Moving right
                    self.rect.right = ground.rect.left
                elif self.accx < 0:  # Moving left
                    self.rect.left = ground.rect.right
                self.accx = 0  # Stop horizontal movement on collision

    def handle_vertical_collisions(self):
        self.grounded = False  # Assume player is not grounded
        for ground in self.grounds:
            if self.rect.colliderect(ground.rect):
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
        #pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)
        self.update()

    def set_ground(self, grounds):
        self.grounds = grounds

# camera.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self):
        self.camera = pygame.Vector2(0, 0)
        self.smooth = 0.1  # Adjust this for smoother or more abrupt camera movement

    def update(self, target):
        # Smoothly adjust the camera to follow the player
        delta_x = (target.rect.x + target.rect.width / 2) - (self.camera.x + SCREEN_WIDTH / 2)
        delta_y = (target.rect.y + target.rect.height / 2) - (self.camera.y + SCREEN_HEIGHT / 2)
        self.camera += pygame.Vector2(delta_x * self.smooth, delta_y * self.smooth)

    def apply_position(self, rect):
        # Adjust object position based on camera offset
        return rect.move(-self.camera.x, -self.camera.y)

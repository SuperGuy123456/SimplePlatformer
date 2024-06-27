from settings import *
import pygame
class Camera:
    def __init__(self, width, height, level_width, level_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.level_width = level_width * TILE_SIZE  # Total width of the level in pixels
        self.level_height = level_height * TILE_SIZE  # Total height of the level in pixels

    def apply_position(self, entity_rect):
        return entity_rect.move(self.camera.x, -self.camera.y)

    def apply_offset(self, offset):
        return offset[0] - self.camera.x, offset[1] - self.camera.y

    def update(self, target):
        # Calculate the desired center of the camera based on the target's position
        target_x = target.rect.centerx
        target_y = target.rect.centery

        # Calculate the new camera position based on the target's position and screen dimensions
        x = -target_x + self.width / 2
        y = -target_y + self.height / 2

        # Clamp camera to the level boundaries
        x = min(0, x)  # Left boundary
        x = max(-(self.level_width - self.width), x)  # Right boundary
        y = max(-(self.level_height - self.height), y)  # Bottom boundary
        y = min(0, y)  # Top boundary

        self.camera = pygame.Rect(x, y, self.width, self.height)

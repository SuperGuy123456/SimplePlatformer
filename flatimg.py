class Flat:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply_position(self.rect))
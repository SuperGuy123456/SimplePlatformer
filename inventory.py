import pygame
pygame.init()
class Inventory:
    def __init__(self, size):
        self.size = size
        self.rects = []
        x = 0
        for i in range(size):
            self.rects.append(pygame.Rect(x, 450, 30, 30))
            x += 30
        self.blits = []
        self.imagex = 0
        self.heighlightindex = 0

    def set_inv(self, blits, imagex):
        self.blits = blits
        self.imagex = imagex

    def select(self, index):
        self.heighlightindex = index

    def draw(self, surface):
        for i in self.rects:
            pygame.draw.rect(surface, (255, 255, 255), i, 1)
        for i, (item, pos) in enumerate(self.blits):
            if i == self.heighlightindex:
                # Draw highlight
                pygame.draw.rect(surface, (255, 255, 0), (pos[0],450, 30, 30), 2)
            surface.blit(item.image, (pos[0],450))

        

    def add_item(self, item):
        if len(self.blits) < self.size:
            self.blits.append((item, (self.imagex, 0)))
            self.imagex += 30

import pygame
from tkinter.filedialog import askopenfilename,asksaveasfilename

pygame.init()

screen = pygame.display.set_mode((800, 600))
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self,e):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and e.type == pygame.MOUSEBUTTONDOWN:
            return True
        else:
            return False

run = True
upload = Button(0, 0, pygame.image.load("assets/decor.png"))
while run:
    screen.fill((0, 0, 0))
    upload.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if upload.update(event):
            pass
pygame.quit()
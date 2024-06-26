import pygame 
pygame.init()

class Inventory(pygame.sprite.Sprite):
    def __init__(self,size):
        super().__init__()
        self.size = size
        self.slots = []
        self.blits = []
        self.heighlightindex = 0
        x = 0
        for i in range(self.size):
            self.slots.append(pygame.Rect(x,450,30,30))
            x+= 30
        self.imagex = 0
    
    def draw(self,screen):
        counter = 0
        for slot in self.slots:
            if counter == self.heighlightindex:
                pygame.draw.rect(screen,(255,255,255),slot,2)
            else:
                pygame.draw.rect(screen,(255,255,255),slot,1)
            counter += 1
        for i in self.blits:
            screen.blit(i[0].image,i[1])

    def select(self,index):
        self.heighlightindex = index

    def set_inv(self,blits,imagex):
        self.blits = blits
        self.imagex = imagex

    def add_item(self,item):
        self.blits.append((item,(self.imagex,450)))
        self.imagex += 30
        

import pygame
from time import time
pygame.init()

class HUD(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.player = player
        self.font = pygame.font.SysFont('comicsans', 20)
    
    def draw(self,screen):
        if self.player.active_effect != None:
            text = self.font.render("Effect: "+self.player.active_effect+", Duration: "+str(round(self.player.effect_duration - (time() - self.player.effect_start_time))), True, (255,255,255))
            screen.blit(text, (0,25))
        else:
            text = self.font.render("Effect: None", True, (255,255,255))
            screen.blit(text, (0,25))

        text = self.font.render("Coins: "+str(self.player.coins), True, (255,255,255))
        screen.blit(text, (0,45))
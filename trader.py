import pygame
import settings
from item import Item

pygame.init()

class Trader(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = settings.trader
        self.inter = settings.interact
        self.interrect = self.inter.get_rect()
        self.interrect.x = x
        self.interrect.y = y - 5
        self.drawinterrect = False
        self.index = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.accx = 0
        self.accy = 0
        self.grounded = False
        self.current_ground = None
        self.air_control_factor = 0.5
        self.max_speed = 5
        self.type = type
        self.potions = {"Strength Potion": "strength", "Speed Potion": "speed", "Health Potion": "health", "Jump Potion": "jump", "Invisibility Potion": "invisible"}
        self.images = [settings.stampotion,settings.strengthpotion,settings.healthpotion, settings.jumppotion,settings.invispotion]
        if self.type == "Common Trader":
            self.sale = {"Speed Potion": 2, "Strength Potion": 3}
        elif self.type == "Rare Trader":
            self.sale = {"Speed Potion": 1, "Strength Potion": 2, "Health Potion": 2, "Jump Potion": 2}
        elif self.type == "Epic Trader":
            self.sale = {"Speed Potion": 0, "Strength Potion": 0, "Health Potion": 0, "Jump Potion": 0, "Invisibility Potion": 0}
        self.font = pygame.font.SysFont('comicsans', 15)
        self.text = []
        self.salerects = []
        y = 0
        text = self.font.render("Shopping from the " + self.type, True, (255, 255, 255))
        self.text.append((text, pygame.Rect(360, y, text.get_width(), text.get_height())))
        y += 20
        for name, cost in self.sale.items():
            text = self.font.render(name + ": " + str(cost), True, (255, 255, 255))
            rect = text.get_rect()
            rect.x = 360
            rect.y = y
            self.salerects.append(rect)
            camrect = pygame.Rect(360, y, text.get_width(), text.get_height())
            self.text.append((text, camrect))
            y += 20
        self.shopping = False

    def checkforsale(self, e):
        for index, rect in enumerate(self.salerects):
            if rect.collidepoint(pygame.mouse.get_pos()) and e.type == pygame.MOUSEBUTTONDOWN:
                item = list(self.sale.keys())[index]
                name_index = 0
                potionname = ""
                for i, name in self.potions.items():
                    if i == item:
                        name_index = index
                        potionname = name
                image = self.images[name_index]
                cost = self.sale[item]
                print(name_index)
                print(item, " or ", potionname, " for ", cost, " which looks like ", image)
                if self.player.coins >= cost:
                    self.player.coins -= cost
                    self.player.inventory.add_item(Item(0,0, image, potionname))
                else:
                    print("You don't have enough coins")
                return potionname
        return None

    def update(self):
        if self.player.attack_rect.colliderect(self.rect):
            self.drawinterrect = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.shopping = True
            if keys[pygame.K_d]:
                self.shopping = False
        else:
            self.drawinterrect = False
            self.shopping = False
        
        if self.accx > self.max_speed:
            self.accx = self.max_speed
        elif self.accx < -self.max_speed:
            self.accx = -self.max_speed

        self.rect.x += self.accx
        self.handle_horizontal_collisions()

        self.rect.y += self.accy
        self.handle_vertical_collisions()
        self.interrect.x = self.rect.x + 10
        self.interrect.y = self.rect.y - 10

        if not self.grounded:
            self.accy += 0.8

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

    def handle_horizontal_collisions(self):
        for ground in self.grounds:
            if self.rect.colliderect(ground):
                if self.accx > 0:
                    self.rect.right = ground.rect.left
                elif self.accx < 0:
                    self.rect.left = ground.rect.right
                self.accx = 0

    def handle_vertical_collisions(self):
        self.grounded = False
        for ground in self.grounds:
            if self.rect.colliderect(ground):
                if self.accy > 0:
                    self.rect.bottom = ground.rect.top
                    self.grounded = True
                    self.current_ground = ground
                elif self.accy < 0:
                    self.rect.top = ground.rect.bottom
                self.accy = 0
        if not self.grounded:
            self.current_ground = None

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply_position(self.rect))
        if self.shopping:
            for text in self.text:
                surface.blit(text[0], text[1])
        if self.drawinterrect:
            surface.blit(self.inter, camera.apply_position(self.interrect))
        self.update()

    def set_ground(self, grounds):
        self.grounds = grounds

    def set_enemies(self, enemies):
        self.enemies = enemies

    def set_items(self, items):
        self.items = items

    def set_decors(self, decors):
        self.decors = decors
    
    def set_player(self, player):
        self.player = player

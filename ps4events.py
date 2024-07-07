import pygame

pygame.init()

class PS4:
    def __init__(self):
        self.con = pygame.joystick.Joystick(0)
        self.keys = ["X", "Circle","Square","Triangle","Share","PS","Options","Leftjoystick","Rightjoystick","L1","R1","Dup","Ddown","Dleft","Dright"]

    def getkeys(self):
        keys = pygame.key.get_pressed()
        if keys.type[pygame.JOYBUTTONDOWN]:
            return self.keys[keys.button]
        '''if event.type == pygame.JOYBUTTONDOWN:
            return self.keys[event.button]'''

        return None

    def vibrate(self, minvib = 0, maxvib = 0.3,duration = 200):

        self.con.rumble(minvib, maxvib, duration)


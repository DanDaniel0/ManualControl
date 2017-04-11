from Game_Constants import *
import pygame
import random
class Conveyor(pygame.sprite.Sprite):
    def __init__(self, begin_factory, end_factory, x, y, game, prev_dir='Up'):
        super(Conveyor, self).__init__()
        self.image = pygame.image.load('images/ConveyorBelt1.png')
        self.originalImage = self.image
        self.straightImages = []
        self.turnImages = []
        for i in range(1,15):
            self.straightImages.append(pygame.image.load('images/ConveyorBelt%s.png' % i))
        for i in range(1,5):
            self.turnImages.append(pygame.image.load('images/Turn%s.png' % i).convert_alpha())
        self.rect = self.image.get_rect()
        self.game = game
        self.begin_factory = begin_factory
        self.end_factory = end_factory
        self.x = x
        self.y = y
        self.rect.topleft = (x,y)
        self.end_factory.conveyors.append(self)
        self.dir = None
        if abs(self.y - end_factory.y) > 0.25:
            if self.y - end_factory.y < 0:
                self.dir = 'Up'
                self.image = pygame.transform.rotate(self.image,90)
                self.originalImage = self.image
                newConveyor = Conveyor(self.begin_factory, self.end_factory, self.x, self.y + (0.125 * 4/3), self.game, self.dir)
                self.game.allConveyorSprites.add(newConveyor)
            else:
                self.dir = 'Down'
                self.image = pygame.transform.rotate(self.image,-90)
                self.originalImage = self.image
                newConveyor = Conveyor(self.begin_factory, self.end_factory, self.x, self.y - (0.125 * 4/3), self.game,self.dir)
                self.game.allConveyorSprites.add(newConveyor)

        elif abs(self.x - self.end_factory.x) > 0.25:
            if self.x - self.end_factory.x < 0:
                self.dir = 'Right'
                newConveyor = Conveyor(self.begin_factory, end_factory, self.x + 0.125, self.y,self.game,self.dir)
                self.game.allConveyorSprites.add(newConveyor)
            else:
                self.dir = 'Left'
                self.image = pygame.transform.rotate(self.image,180)
                self.originalImage = self.image
                newConveyor = Conveyor(self.begin_factory, end_factory, self.x - 0.125, self.y,self.game,self.dir)
                self.game.allConveyorSprites.add(newConveyor)

    def update(self, scale, screen):
        if self.dir == 'Right' or self.dir == 'Left':
            pygame.draw.rect(screen, (76, 174, 255), (WINDOW_WIDTH/2 + self.x * scale, WINDOW_HEIGHT/2 + self.y * scale, 35 * scale/200, 6 * scale/200), 0)
            pygame.draw.rect(screen, (76, 174, 255), (WINDOW_WIDTH/2 + self.x * scale, 35 * scale/200 + WINDOW_HEIGHT/2 + self.y * scale, 35 * scale/200, 6 * scale/200), 0)
        else:
            pygame.draw.rect(screen, (76, 174, 255), (WINDOW_WIDTH/2 + self.x * scale, WINDOW_HEIGHT/2 + self.y * scale, 6 * scale/200, 35 * scale/200), 0)
            pygame.draw.rect(screen, (76, 174, 255), (35 * scale/200 + WINDOW_WIDTH/2 + self.x * scale, WINDOW_HEIGHT/2 + self.y * scale, 6 * scale/200, 35 * scale/200), 0)

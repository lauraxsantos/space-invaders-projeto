import pygame


class Aliens(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('alien02.png')
        self.rect = self.image.get_rect(center=pos)

    def update(self, velocity):
        self.rect.x += velocity

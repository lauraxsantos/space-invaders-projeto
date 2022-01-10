import pygame


class Coracao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coracao.png')
        self.rect = self.image.get_rect(right=x, top=y)

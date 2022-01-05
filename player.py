import pygame


class Player:
    def __init__(self, pos):
        self.img = pygame.image.load('spaceship.png')
        self.rect = self.img.get_rect(midbottom=pos)

    def desenhar(self, tela):
        tela.blit(self.img, self.rect)

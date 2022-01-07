import pygame


class Atirar(pygame.sprite.Sprite):
    # sprite do laser do jogador
    def __init__(self, pos, velocity, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = velocity

    def update(self):
        self.rect.y += self.velocity
        if self.rect.y < 0 or self.rect.y > 900:
            self.kill()

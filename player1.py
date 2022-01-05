import pygame


class Player:
    def __init__(self, pos, velocity, limit):
        self.img = pygame.image.load('spaceship.png')
        self.rect = self.img.get_rect(midbottom=pos)
        self.velocity = velocity
        self.limit_x = limit

    def run(self, tela):
        self.move()
        self.limit_player()
        tela.blit(self.img, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity

    def limit_player(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.limit_x:
            self.rect.right = self.limit_x

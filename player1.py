import pygame
from atirar import Atirar


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, limit):
        pygame.sprite.Sprite.__init__(self)

        # desenho
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect(midbottom=pos)

        self.keys = pygame.key.get_pressed()    # inputs do teclados
        self.velocity = velocity                # velocidade da nave
        self.limit_x = limit

        # recarregar
        self.reloading = False
        self.start_reload = 0
        self.time_reload = 600

        self.tiros = pygame.sprite.Group()

    def update(self):
        self.get_input()                # verifica os inputs do teclado
        self.reloaded()                 # verifica se o playaer pode disparar
        self.limits_player()
        self.tiros.update()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_SPACE] and not self.reloading:
            self.disparo()
            self.reloading = True
            self.start_reload = pygame.time.get_ticks()

    def disparo(self):
        pygame.mixer.music.load('tiros_player.mp3')
        self.tiros.add(Atirar(self.rect.center, -5, "blue"))
        pygame.mixer.music.play()

    def reloaded(self):
        if self.reloading:
            elapsed = pygame.time.get_ticks()
            if elapsed - self.start_reload >= self.time_reload:
                self.reloading = False

    def limits_player(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.limit_x:
            self.rect.right = self.limit_x

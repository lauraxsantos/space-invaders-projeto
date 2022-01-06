import pygame
from sys import exit

pygame.init()


largura = 500
altura = 440
velocidade = 5

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

plano_de_fundo = pygame.image.load("sprites/plano de fundo.png")


class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/spaceship.png")
        self.image = pygame.transform.scale(self.image, (60, 53))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.tiro = pygame.time.get_ticks()

    def teclas(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.left -= velocidade
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.rect.right <= 595:
            self.rect.right += velocidade
        tempo_atirar = pygame.time.get_ticks()
        espera_laser = 550
        # milisegundos
        # quando aperta espaço se o tempo em que a função for chamada menos o tempo onde o último disparo foi efetuado for maior que o tempo de espera, dispara o laser
        if pygame.key.get_pressed()[pygame.K_SPACE] and tempo_atirar - self.tiro >= espera_laser:
            laser = Atirar(self.rect.centerx, self.rect.top)
            atirar_gp.add(laser)
            self.tiro = pygame.time.get_ticks()


class Atirar(pygame.sprite.Sprite):
    # sprite do laser do jogador
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 10))
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()


nave = Jogador(int(largura / 2), altura - 50)
nave_gp = pygame.sprite.Group()
nave_gp.add(nave)
atirar_gp = pygame.sprite.Group()

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    tela.blit(plano_de_fundo, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    nave.teclas()

    nave_gp.update()
    atirar_gp.update()

    atirar_gp.draw(tela)
    nave_gp.draw(tela)

    pygame.display.flip()

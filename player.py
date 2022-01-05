import pygame
from sys import exit

pygame.init()

x = 300
y = 350
largura = 680
altura = 440
velocidade = 5

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

imgjogador = pygame.image.load("sprites/spaceship.png")
jogador = pygame.transform.scale(imgjogador, (60, 53))


def desenhojogador():
    tela.blit(jogador, (x, y))


while True:
    relogio.tick(55)
    tela.fill((0, 0, 0))

    desenhojogador()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if x <= 0:
        pass
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        x -= velocidade
    if x >= 620:
        pass
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        x += velocidade


    pygame.display.update()

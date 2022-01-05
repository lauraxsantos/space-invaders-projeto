import pygame
from sys import exit
from player import Player


class Game:
    def __init__(self):
        player_sprite = Player((340, 360))
        self.player = player_sprite

    def run(self):
        self.player.desenhar(tela)


pygame.init()

# configs da tela
largura = 680
altura = 440
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

game = Game()   # Atribui o Game() a game

while True:
    relogio.tick(32)
    tela.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game.run()

    pygame.display.update()

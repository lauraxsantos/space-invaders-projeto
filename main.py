import pygame
from sys import exit
from player1 import Player
from aliens import Aliens
from random import choice
from atirar import Atirar


class Game:
    def __init__(self):

        # player
        player_sprite = Player((largura/2, altura-10), 5, largura)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # aliens
        self.aliens = pygame.sprite.Group()
        self.create_aliens(100, 100, 25, 8, 8)
        self.aliens_velocity = 1

        # atierar dos aliens
        self.reloading_aliens = False
        self.start_reload = 0
        self.time_reload = 800
        self.tiro_aliens = pygame.sprite.Group()

    # criar múltiplos aliens
    def create_aliens(self, padding_start_x, padding_start_y, distance_aliens, nx_aliens, ny_aliens):
        for c in range(ny_aliens):
            for r in range(nx_aliens):
                x = padding_start_x + r * (distance_aliens + 50)
                y = padding_start_y + c * (distance_aliens + 25)
                self.aliens.add(Aliens((x, y)))

    # movimento dos aliens
    def direction_aliens(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= largura:
                self.aliens_velocity = -1
                self.move_down()
            if alien.rect.left <= 0:
                self.aliens_velocity = 1
                self.move_down()

    def move_down(self):
        if self.aliens:
            all_aliens = self.aliens.sprites()
            for alien in all_aliens:
                alien.rect.y += 1

    # disparos dos aliens
    def atirar_aliens(self):
        if not self.reloading_aliens:
            alien_escolhido = choice(self.aliens.sprites())
            self.tiro_aliens.add(Atirar(alien_escolhido.rect.center, 5, "green"))
            self.reloading_aliens = True
            self.start_reload = pygame.time.get_ticks()

    # tempo entre cada disparo dos aliens
    def reload(self):
        if self.reloading_aliens:
            elapsed = pygame.time.get_ticks()
            if elapsed - self.start_reload >= self.time_reload:
                self.reloading_aliens = False

    def run(self):
        self.reload()
        self.atirar_aliens()

        self.tiro_aliens.update()
        self.aliens.update(self.aliens_velocity)
        self.direction_aliens()
        self.player.update()

        # desenhos
        self.tiro_aliens.draw(tela)
        self.player.sprite.tiros.draw(tela)
        self.aliens.draw(tela)
        self.player.draw(tela)


pygame.init()

# configs da tela
largura = int(pygame.display.Info().current_w // 2)
altura = int(pygame.display.Info().current_h * .95)
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

game = Game()   # Atribui o Game() a game

while True:
    relogio.tick(60)
    tela.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game.run()

    pygame.display.update()

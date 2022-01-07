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
    # cria a sprite do jogador
    # o def __init___(self) inicia a classe é uma função obrigatória, depois vc coloca os parâmetros (se tiver) 
    # o pygame.sprite.Sprite é um parâmetro do próprio pygame pra utilizar classes e criar sprites
    # as instâncias nas classes começam com self
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/spaceship.png")
        self.image = pygame.transform.scale(self.image, (60, 53))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.tiro = pygame.time.get_ticks()
      
    # Você pode criar outras funções (além da principal) específicas dentro da classe      
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
        # coloco a classe Atirar dentro da variável laser e adiciono ao grupo de sprites
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

            
class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.image = pygame.image.load("sprites/alien3.png")
        self.image = pygame.transform.scale(self.image, (30, 23))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.mov = 1
        self.cont = 0

    def update(self):
        #  move o retângulo dos aliens para a direita
        # quando o contador chega a 80 o alien da ponta chega na borda da tela
        # então o valor do movimento  fica negativo para ele começar a se mover para esquerda
        self.rect.x += self.mov
        self.cont += 1
        if abs(self.cont) > 80:
            self.mov *= -1
            if self.mov > 0:
                self.cont = 0
            if self.mov < 0:
                self.cont = -80 

# grupos de sprites
# chamo a função e coloco dentro da variável nave, depois crio um grupo de sprites e adiciono a variável nele
nave = Jogador(int(largura / 2), altura - 50)
nave_gp = pygame.sprite.Group()
nave_gp.add(nave)
atirar_gp = pygame.sprite.Group()
aliens_gp = pygame.sprite.Group()

# cria os aliens na tela como uma matriz
for linha in range(4):
    for coluna in range(4):
        alien = Aliens(100 + linha * 100, 50 + coluna * 50)
        aliens_gp.add(alien)

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    tela.blit(plano_de_fundo, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # coloquei a classe Jogador dentro da variável nave e chamei a função teclas
    nave.teclas()
    
   # atualizando as classes a cada looping    
    nave_gp.update()
    atirar_gp.update()
    aliens_gp.update()
    
    # aqui eu desenho o que tem nos grupos de sprites (as sprites)    
    atirar_gp.draw(tela)
    nave_gp.draw(tela)
    aliens_gp.draw(tela)
    
    pygame.display.flip()

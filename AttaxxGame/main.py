import pygame 


from classes.jogo import Jogo
from confg import *


jogo = Jogo()

#jogo.start()

screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


while True:

    jogo.tabuleiro.desenha_tabuleiro(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()  # Or pygame.display.flip()
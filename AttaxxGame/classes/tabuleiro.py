import os
import random
import pygame

from confg import *


class Tabuleiro:
    def __init__(self):
        #self.path = os.path.join(TABULEIROS_PATH,random.choice(os.listdir(TABULEIROS_PATH)))
        self.path = "tabuleiros/tab4.txt"
        self.monta_tabuleiro(self.path)


    def monta_tabuleiro(self, path):
        self.tabuleiro = []
        with open(path) as file:
            self.size = int(file.readline())
            for i in range(self.size):
                linha = file.readline().rstrip('\n ').split(" ")
                linha = list(map(int, linha))
                self.tabuleiro.append(linha)
            

    def printa_tabuleiro(self):
        print("--------------")
        for linha in self.tabuleiro:
            print(linha)
        print("--------------")


    def rem_valor_tabuleiro(self, posicao):
        self.tabuleiro[posicao[0]][posicao[1]] = 0


    def add_valor_tabuleiro(self, posicao, valor):
        self.tabuleiro[posicao[0]][posicao[1]] = valor


    def tabuleiro_completo(self):
        jg1_count = 0
        jg2_count = 0
        for linha in self.tabuleiro:
            for valor in linha:
                if valor == 0:
                    return False, None
                elif valor == 1:
                    jg1_count+=1
                elif valor == 2:
                    jg2_count+=1
        return True, (jg1_count,jg2_count)


    def desenha_tabuleiro(self, tela):
        '''
            Desenha Tabuleiro Usando Pygame
        '''
        for i,linha in enumerate(self.tabuleiro):
            for j,valor in enumerate(self.tabuleiro):
                cor = VERMELHO
                if (i+j)%2 == 0: cor = BRANCO
                pygame.draw.rect(tela, cor, pygame.Rect(i*TAMANHO_QUADRADO, j*TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO)) 

import os
import random

from confg import TABULEIROS_PATH


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
        for linha in self.tabuleiro:
            for valor in linha:
                if valor == 0:
                    return False
        return True

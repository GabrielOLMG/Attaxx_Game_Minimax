from classes.tabuleiro import Tabuleiro
from confg import PRIMEIRO_JOGADOR


class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()

        self.proximo_jogador = PRIMEIRO_JOGADOR
        self.turnos = 0 # Quantidade de turnos
        pass


    def start(self):
        self.jogo(self.proximo_jogador)


    def jogo(self, jogador_vez):
        print(f"VEZ DO JOADOR {jogador_vez}")

        self.tabuleiro.printa_tabuleiro()
        self.turno_player(jogador_vez)

        if self.tabuleiro.tabuleiro_completo():
            self.fim_jogo()
            return

        self.jogo(1 if jogador_vez == 2 else 2)
    

    def turno_player(self, jogador):
        selecionado_linha = input("Qual Linha esta a peça? ")
        selecionado_coluna = input("Qual coluna esta a peça? ")

        proxima_linha = input("Qual Linha vai a peça? ")
        proxima_coluna = input("Qual coluna vai a peça? ")

        atual   = (int(selecionado_linha)-1, int(selecionado_coluna)-1)
        proximo = (int(proxima_linha)-1, int(proxima_coluna)-1)

        jogada_valida = self.verifica_jogada(proximo, atual, jogador)

        self.consequencia_jogada(jogada_valida, atual, proximo, jogador)
        

    

    def verifica_jogada(self, proximo, atual, jogador):
        '''

        return:
            0 = MOVIMENTAÇÃO INVALIDA - REFAZ A JOGADA
            1 = CLONA A PEÇA 
            2 = MOVE A PEÇA
        '''
        tabuleiro = self.tabuleiro.tabuleiro

        # Selecionou a peça certa?
        if tabuleiro[atual[0]][atual[1]] != jogador:
            return 0

        # Fora do tabuleiro?
        if proximo[0] < 0 or proximo[0] >= self.tabuleiro.size or \
           proximo[1] < 0 or proximo[1] >= self.tabuleiro.size:
            return 0
        
        # Poicao Ja ocupada?
        if tabuleiro[proximo[0]][proximo[1]] in ['8' ,'1', '2']:
            return 0
        
        # Esta perto da atual?
        if abs(atual[0]-proximo[0]) <= 2 and abs(atual[1]-proximo[1]) <= 2:
            if abs(atual[0]-proximo[0]) <= 1 and abs(atual[1]-proximo[1]) <= 1:
                return 1
            else:
                return 2
        
        return -1


    def consequencia_jogada(self, flag, atual, proximo, jogador):
        '''
            FALTA FAZER COM QUE ELE TRANSFORME AS PEÇAS NA COR DESEJADA,
            SE TIVER PERTO DE ALGUMA
        '''
        if flag == 1:
            self.tabuleiro.add_valor_tabuleiro(proximo,jogador)
        elif flag == 2:
            self.tabuleiro.rem_valor_tabuleiro(atual)
            self.tabuleiro.add_valor_tabuleiro(proximo,jogador)
        else:
            print("JOGADA IMPOSSIVEL - refaça")
            self.turno_player(jogador)
            return

        self.lista_oponentes_perto(proximo, jogador)        
        
    
    def lista_oponentes_perto(self, proximo, jogador):
        '''
            return:
                lista com as posições onde estão os inimigos por perto
        '''
        jogador_inimigo = 2 if jogador == 1 else 1
        tabuleiro = self.tabuleiro.tabuleiro

        coordenadas_inimigo = []

        possiveis_colunas = list(range(max(0,proximo[1]-1),min(self.tabuleiro.size -1,proximo[1]+1)+1))
        if proximo[0] != 0:
            # verifica linha de cima:
            for i in possiveis_colunas:
                atual = tabuleiro[proximo[0]+1][i]
                if atual == jogador_inimigo:
                    coordenadas_inimigo.append([proximo[0]+1,i])

        if proximo[0] < self.tabuleiro.size:
            # verifica linha de baixo:
            for i in possiveis_colunas:
                atual = tabuleiro[proximo[0]-1][i]
                if atual == jogador_inimigo:
                    coordenadas_inimigo.append([proximo[0]-1,i])
        
        # varifica laterais
        if proximo[1]-1 >= 0 and tabuleiro[proximo[0]][proximo[1]-1] == jogador_inimigo:
            coordenadas_inimigo.append([proximo[0],proximo[1]-1])

        if proximo[1]+1 < self.tabuleiro.size and tabuleiro[proximo[0]][proximo[1]+1] == jogador_inimigo:
            coordenadas_inimigo.append([proximo[0],proximo[1]+1])
        print(coordenadas_inimigo)




    def fim_jogo(self):
        self.tabuleiro.printa_tabuleiro()
        print("FIM DO JOGO")
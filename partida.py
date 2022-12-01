import pygame
from Player import Player
from Campo import Campo
from Estremidade import Estremidade
from Point import Point
from Bola import Bola
from Controle_player import Controle_player
from Especial import Especial
import random
import sys


class Partida:
    def __init__(self, display, player1, player2, campo):
        self.display = display
        self.player1 = player1
        self.player1.set_posicao(250, 570)
        self.player2 = player2
        self.player2.set_posicao(250, 30)
        self.campo = campo
        self.placar_p1 = 0
        self.placar_p2 = 0
        self.placar_maximo = 10

        if 'ubuntumono' in pygame.font.get_fonts():
            font = 'ubuntumono'
        else:
            font = pygame.font.get_default_font()
        self.font_placar = pygame.font.SysFont(font, 35)
        self.font_text_inicio = pygame.font.SysFont(font, 50)

        vy = 10
        vx = random.randint(-10, 10)
        self.bola = Bola(1, [vx, (vy if random.random() < 0.5 else -vy)], campo)
        self.especiais = Especial(self.bola, self)
        self.relogio = pygame.time.Clock()
        self.key_pressed = []

        self.animacao_inicio_partida()
        self.loop()
        self.animacao_final_partida(1 if self.placar_p1 == self.placar_maximo else 2)

    def loop(self):
        while self.placar_p1 < self.placar_maximo and self.placar_p2 < self.placar_maximo:
            pygame.event.pump()
            self.get_eventos()
            self.display.fill([0, 0, 0])
            self.relogio.tick(30)
            self.campo.draw(self.display)
            self.player1.get_evento(self.key_pressed, self.especiais)
            self.player1.draw(self.display)
            self.player2.get_evento(self.key_pressed, self.especiais)
            self.player2.draw(self.display)
            self.bola.draw(self.display, self.campo, self.player1.retang, self.player2.retang, self.especiais, self)
            self.especiais.draw(self.display)
            self.placar()
            pygame.display.flip()

    def get_eventos(self):
        for event in pygame.event.get(pygame.KEYDOWN):
            self.key_pressed.append(event.key)

        for event in pygame.event.get(pygame.KEYUP):
            self.key_pressed.remove(event.key)

        if len(pygame.event.get(pygame.QUIT)) != 0:
            sys.exit()

    def ponto_marcado(self, player):
        self.especiais.apagar_bolas_p1()
        self.especiais.apagar_bolas_p2()
        self.bola.set_posicao_inicial_centro(self.campo)
        if player == 1:
            self.placar_p1 += 1
            if self.bola.vetor[1] < 0:
                self.bola.vetor[1] = -self.bola.vetor[1]
                self.bola.vetor[0] = random.randint(-10, 10)
        if player == 2:
            self.placar_p2 += 1
            if self.bola.vetor[1] > 0:
                self.bola.vetor[1] = -self.bola.vetor[1]
                self.bola.vetor[0] = random.randint(-10, 10)

        self.especiais.resetar()
        if self.placar_p1 < self.placar_maximo and self.placar_p2 < self.placar_maximo:
            self.animacao_ponto_marcado(player)

    def animacao_inicio_partida(self):
        cont = 0
        indice = 0

        branco = [255, 255, 255]
        self.bola.vetor[1] = self.bola.vetor[1] / 4
        self.bola.vetor[0] = self.bola.vetor[0] / 4
        text = ["Inicio de Partida", "Preparar", "Apontar", "Vai..."]
        duracao = [25, 15, 10, 10, 10]
        while 1:
            cont += 1
            if cont == duracao[indice]:
                cont = 0
                indice += 1
                if indice > 3:
                    break

            pygame.event.pump()
            self.get_eventos()
            self.display.fill([0, 0, 0])
            self.relogio.tick(30)
            self.campo.draw(self.display)
            self.player1.get_evento(self.key_pressed, self.especiais)
            self.player1.draw(self.display)
            self.player2.get_evento(self.key_pressed, self.especiais)
            self.player2.draw(self.display)
            self.bola.draw(self.display, self.campo, self.player1.retang, self.player2.retang, self.especiais, self)
            self.especiais.draw(self.display)
            self.placar()

            text_imag = self.font_text_inicio.render(text[indice], True, branco)
            text_rec = text_imag.get_rect()
            text_rec.center = self.campo.meio_de_campo
            self.display.blit(text_imag, text_rec)

            pygame.display.flip()

        self.bola.vetor[1] = self.bola.vetor[1] * 4
        self.bola.vetor[0] = self.bola.vetor[0] * 4

    def animacao_ponto_marcado(self, player):
        cont = 0
        indice = 0

        branco = [255, 255, 255]
        self.bola.vetor[1] = self.bola.vetor[1] / 4
        self.bola.vetor[0] = self.bola.vetor[0] / 4
        text = [str(self.placar_p1) + " X " + str(self.placar_p2), "Reiniciando Partida", "Preparar", "Apontar",
                "Vai..."]
        duracao = [35, 20, 10, 10, 10]
        while 1:
            cont += 1
            if cont == duracao[indice]:
                cont = 0
                indice += 1
                if indice > 4:
                    break

            pygame.event.pump()
            self.get_eventos()
            self.display.fill([0, 0, 0])
            self.relogio.tick(30)
            self.campo.draw(self.display)
            self.player1.get_evento(self.key_pressed, self.especiais)
            self.player1.draw(self.display)
            self.player2.get_evento(self.key_pressed, self.especiais)
            self.player2.draw(self.display)
            self.bola.draw(self.display, self.campo, self.player1.retang, self.player2.retang, self.especiais, self)
            self.especiais.draw(self.display)
            self.placar()

            text_imag = self.font_text_inicio.render(text[indice], True, branco)
            text_rec = text_imag.get_rect()
            text_rec.center = self.campo.meio_de_campo
            self.display.blit(text_imag, text_rec)

            pygame.display.flip()

        self.bola.vetor[1] = self.bola.vetor[1] * 4
        self.bola.vetor[0] = self.bola.vetor[0] * 4

    def animacao_final_partida(self, vencedor):
        cont = 0
        indice = 0

        branco = [255, 255, 255]
        text = ["Fim de Partida", str(self.placar_p1) + " X " + str(self.placar_p2),
                "Player " + str(vencedor) + " Venceu"]
        duracao = [60, 45, 80]
        while 1:
            cont += 1
            if cont == duracao[indice]:
                cont = 0
                indice += 1
                if indice > 2:
                    break

            pygame.event.pump()
            self.get_eventos()
            self.display.fill([0, 0, 0])
            self.relogio.tick(30)
            self.campo.draw(self.display)
            self.player1.get_evento(self.key_pressed, self.especiais)
            self.player1.draw(self.display)
            self.player2.get_evento(self.key_pressed, self.especiais)
            self.player2.draw(self.display)
            self.especiais.draw(self.display)
            self.placar()

            text_imag = self.font_text_inicio.render(text[indice], True, branco)
            text_rec = text_imag.get_rect()
            text_rec.center = self.campo.meio_de_campo
            self.display.blit(text_imag, text_rec)

            pygame.display.flip()

    def placar(self):
        verde = [0, 255, 0]
        text1 = self.font_placar.render(str(self.placar_p1), True, verde)
        text1_rec = text1.get_rect()
        text1_rec.center = 35, 350  # colocar em uma variavel esta posição
        self.display.blit(text1, text1_rec)

        text2 = self.font_placar.render(str(self.placar_p2), True, verde)
        text2_rec = text2.get_rect()
        text2_rec.center = 35, 250
        self.display.blit(text2, text2_rec)


if __name__ == '__main__':
    size = Largura, Altura = 500, 600

    bottom = Estremidade(Point(10, Altura - 10), Point(Largura - 10, Altura - 10), "marca_ponto")
    top = Estremidade(Point(10, 10), Point(Largura - 10, 10), "marca_ponto")
    left = Estremidade(Point(10, 10), Point(10, Altura - 10), "reflete")
    right = Estremidade(Point(Largura - 10, 10), Point(Largura - 10, Altura - 10), "reflete")

    pygame.init()
    pygame.font.init()

    a = Partida(pygame.display.set_mode(size),
                Player(1, [255, 0, 0], 1, 2, 3, bottom,
                       Controle_player(pygame.K_a, pygame.K_d, pygame.K_g, pygame.K_h, pygame.K_j)),
                Player(2, [255, 0, 0], 1, 2, 3, top,
                       Controle_player(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3)),
                Campo(left, right, top, bottom))

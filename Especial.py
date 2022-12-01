import pygame
from Bola import Bola
import random

# Especial 1 (V): Próxima vez q a bola toca na prancha do player, esta é refletida com o dobro da velocidade.
# Especial 2 (R): Limite anterior do player vai refletir a bola uma vez.
# Especial 3 (C):  Próxima vez q a bola toca na prancha do player, duas bolas são refletidas.
# obs: Todos os especiais são desativados após algum dos players ganhar ponto.


class Especial:
    def __init__(self, bola, partida):
        self.bola = bola
        self.bola2_p1 = None
        self.bola3_p1 = None
        self.bola2_p2 = None
        self.bola3_p2 = None
        self.cont_ticks_p1 = 0
        self.cont_ticks_p2 = 0
        self.posicao_inicial_bolas_p1 = None
        self.vetor_inicial_bolas_p1 = None
        self.posicao_inicial_bolas_p2 = None
        self.vetor_inicial_bolas_p2 = None
        self.partida = partida
        self.font_especial = pygame.font.SysFont('ubuntumono', 20)
        self.posicao_esp_p1 = 400, 550
        self.posicao_esp_p2 = 400, 35

        ## chamada dos especiais
        self.p1_esp1_ch = False
        self.p1_esp2_ch = False
        self.p1_esp3_ch = False

        self.p2_esp1_ch = False
        self.p2_esp2_ch = False
        self.p2_esp3_ch = False

        ## ativacao dos especiais
        self.p1_esp1_at = False
        self.p1_esp2_at = False
        self.p1_esp3_at = False

        self.p2_esp1_at = False
        self.p2_esp2_at = False
        self.p2_esp3_at = False

        ## desativacao dos especiais
        self.p1_esp1_ds = False
        self.p1_esp2_ds = False
        self.p1_esp3_ds = False

        self.p2_esp1_ds = False
        self.p2_esp2_ds = False
        self.p2_esp3_ds = False

    def call(self, id, player):
        if player == 1:
            if id == 1:
                self.p1_esp1_ch = True
            elif id == 2:
                self.p1_esp2_ch = True
                self.p1_esp2_at = True
                self.partida.campo.es_b.reflete = "reflete"
            elif id == 3:
                self.p1_esp3_ch = True
        elif player == 2:
            if id == 1:
                self.p2_esp1_ch = True
            elif id == 2:
                self.p2_esp2_ch = True
                self.p2_esp2_at = True
                self.partida.campo.es_t.reflete = "reflete"
            elif id == 3:
                self.p2_esp3_ch = True

    def colisao_com_p1(self):
        if self.p1_esp3_ch:
            self.p1_esp3_at = True
            self.posicao_inicial_bolas_p1 = self.bola.get_posicao()
            self.vetor_inicial_bolas_p1 = self.bola.vetor

        if self.p1_esp1_ch:
            self.p1_esp1_at = True
            self.bola.vetor[1] = self.bola.vetor[1] * 2

        if self.p2_esp1_at:
            self.p1_esp1_ds = True
            if self.bola.vetor[1] < 0:
                self.bola.vetor[1] = -10
            if self.bola.vetor[1] > 0:
                self.bola.vetor[1] = 10

    def colisao_com_p2(self):
        if self.p2_esp3_ch:
            self.p2_esp3_at = True
            self.posicao_inicial_bolas_p2 = self.bola.get_posicao()
            self.vetor_inicial_bolas_p2 = self.bola.vetor

        if self.p2_esp1_ch:
            self.p2_esp1_at = True
            self.bola.vetor[1] = self.bola.vetor[1] * 2

        if self.p1_esp1_at:
            self.p1_esp1_ds = True
            if self.bola.vetor[1] < 0:
                self.bola.vetor[1] = -10
            if self.bola.vetor[1] > 0:
                self.bola.vetor[1] = 10

    def colisao_com_t(self):
        if self.p2_esp2_at:
            self.p2_esp2_ds = True
            self.partida.campo.es_t.reflete = "marca_ponto"

    def colisao_com_b(self):
        if self.p1_esp2_at:
            self.p1_esp2_ds = True
            self.partida.campo.es_b.reflete = "marca_ponto"

    def draw(self, display):
        if self.p1_esp3_at and not self.p1_esp3_ds:
            self.cont_ticks_p1 += 1
            if self.cont_ticks_p1 == 25:
                self.bola2_p1 = Bola(2, [random.randint(-10, 10), self.vetor_inicial_bolas_p1[1]], self.partida.campo)
                self.bola2_p1.set_posicao_inicial(self.posicao_inicial_bolas_p1[0],self.posicao_inicial_bolas_p1[1] - 5)
            ##if self.cont_ticks_p1 == 60:
              ##  self.bola3_p1 = Bola(2, [random.randint(-10, 10), self.vetor_inicial_bolas_p1[1]], self.partida.campo)
                ##self.bola3_p1.set_posicao_inicial(self.posicao_inicial_bolas_p1[0], self.posicao_inicial_bolas_p1[1] - 5)
                self.p1_esp3_ds = True

        if self.p2_esp3_at and not self.p2_esp3_ds:
            self.cont_ticks_p2 += 1
            if self.cont_ticks_p2 == 25:
                self.bola2_p2 = Bola(2, [random.randint(-10, 10), self.vetor_inicial_bolas_p2[1]], self.partida.campo)
                self.bola2_p2.set_posicao_inicial(self.posicao_inicial_bolas_p2[0],self.posicao_inicial_bolas_p2[1] + 5)
            ##if self.cont_ticks_p2 == 60:
              ##  self.bola3_p2 = Bola(2, [random.randint(-10, 10), self.vetor_inicial_bolas_p2[1]], self.partida.campo)
                ##self.bola3_p2.set_posicao_inicial(self.posicao_inicial_bolas_p2[0], self.posicao_inicial_bolas_p2[1] + 5)
                self.p2_esp3_ds = True


        if self.bola2_p1 != None:
            if self.bola2_p1.draw(display, self.partida.campo, self.partida.player1.retang, self.partida.player2.retang, self, self.partida) == -1:
                self.bola2_p1 = None
        if self.bola3_p1 != None:
            if self.bola3_p1.draw(display, self.partida.campo, self.partida.player1.retang, self.partida.player2.retang, self, self.partida) == -1:
                self.bola3_p1 = None

        if self.bola2_p2 != None:
            if self.bola2_p2.draw(display, self.partida.campo, self.partida.player1.retang, self.partida.player2.retang, self, self.partida) == -1:
                self.bola2_p2 = None
        if self.bola3_p2 != None:
            if self.bola3_p2.draw(display, self.partida.campo, self.partida.player1.retang, self.partida.player2.retang, self, self.partida) == -1:
                self.bola3_p2 = None

        verde = [0, 255, 0]
        vermelho = [255, 20, 0]
        azul = [0, 0, 255]
        cinza = [120, 120, 120]


        self.draw_esp_p1(verde, vermelho, azul, cinza, display)
        self.draw_esp_p2(verde, vermelho, azul, cinza, display)

    def draw_esp_p1(self, verde, verm, azul, cin, display):
        cor = verde
        if self.p1_esp1_ds:
            cor = cin
        elif self.p1_esp1_at:
            cor = verm
        elif self.p1_esp1_ch:
            cor = azul
        esp_1 = self.font_especial.render("V", True, cor)
        esp_1_rec = esp_1.get_rect()
        esp_1_rec.center = self.posicao_esp_p1[0], self.posicao_esp_p1[1]
        display.blit(esp_1, esp_1_rec)

        cor = verde
        if self.p1_esp2_ds:
            cor = cin
        elif self.p1_esp2_at:
            cor = verm
        elif self.p1_esp2_ch:
            cor = azul

        esp_2 = self.font_especial.render("R", True, cor)
        esp_2_rec = esp_2.get_rect()
        esp_2_rec.center = self.posicao_esp_p1[0] + 20, self.posicao_esp_p1[1]
        display.blit(esp_2, esp_2_rec)

        cor = verde
        if self.p1_esp3_ds:
            cor = cin
        elif self.p1_esp3_at:
            cor = verm
        elif self.p1_esp3_ch:
            cor = azul

        esp_3 = self.font_especial.render("C", True, cor)
        esp_3_rec = esp_3.get_rect()
        esp_3_rec.center = self.posicao_esp_p1[0] + 40, self.posicao_esp_p1[1]
        display.blit(esp_3, esp_3_rec)

    def draw_esp_p2(self,verde, verm, azul, cin, display):
        cor = verde
        if self.p2_esp1_ds:
            cor = cin
        elif self.p2_esp1_at:
            cor = verm
        elif self.p2_esp1_ch:
            cor = azul
        esp_1 = self.font_especial.render("V", True, cor)
        esp_1_rec = esp_1.get_rect()
        esp_1_rec.center = self.posicao_esp_p2[0], self.posicao_esp_p2[1]
        display.blit(esp_1, esp_1_rec)

        cor = verde
        if self.p2_esp2_ds:
            cor = cin
        elif self.p2_esp2_at:
            cor = verm
        elif self.p2_esp2_ch:
            cor = azul

        esp_2 = self.font_especial.render("R", True, cor)
        esp_2_rec = esp_2.get_rect()
        esp_2_rec.center = self.posicao_esp_p2[0] + 20, self.posicao_esp_p2[1]
        display.blit(esp_2, esp_2_rec)

        cor = verde
        if self.p2_esp3_ds:
            cor = cin
        elif self.p2_esp3_at:
            cor = verm
        elif self.p2_esp3_ch:
            cor = azul

        esp_3 = self.font_especial.render("C", True, cor)
        esp_3_rec = esp_3.get_rect()
        esp_3_rec.center = self.posicao_esp_p2[0] + 40, self.posicao_esp_p2[1]
        display.blit(esp_3, esp_3_rec)

    def resetar(self):
        if self.p1_esp1_ch or self.p1_esp1_at:
            self.p1_esp1_ch = True
            self.p1_esp1_at = True
            self.p1_esp1_ds = True
            self.p1_esp1_ds = True
            if self.bola.vetor[1] < 0:
                self.bola.vetor[1] = -10
            if self.bola.vetor[1] > 0:
                self.bola.vetor[1] = 10

        if self.p1_esp2_ch or self.p1_esp2_at:
            self.p1_esp2_ch = True
            self.p1_esp2_at = True
            self.p1_esp2_ds = True
            self.partida.campo.es_b.reflete = "marca_ponto"

        if self.p1_esp3_ch or self.p1_esp3_at:
            self.p1_esp3_ch = True
            self.p1_esp3_at = True
            self.p1_esp3_ds = True

        if self.p2_esp1_ch or self.p2_esp1_at:
            self.p2_esp1_ch = True
            self.p2_esp1_at = True
            self.p2_esp1_ds = True
            if self.bola.vetor[1] < 0:
                self.bola.vetor[1] = -10
            if self.bola.vetor[1] > 0:
                self.bola.vetor[1] = 10

        if self.p2_esp2_ch or self.p2_esp2_at:
            self.p2_esp2_ch = True
            self.p2_esp2_at = True
            self.p2_esp2_ds = True
            self.partida.campo.es_t.reflete = "marca_ponto"

        if self.p2_esp3_ch or self.p2_esp3_at:
            self.p2_esp3_ch = True
            self.p2_esp3_at = True
            self.p2_esp3_ds = True

    def apagar_bolas_p1(self):
        if self.p1_esp3_at:
            self.p1_esp3_ds = True
        self.bola2_p1 = None
        self.bola3_p1 = None

    def apagar_bolas_p2(self):
        if self.p2_esp3_at:
            self.p2_esp3_ds = True
        self.bola2_p2 = None
        self.bola3_p2 = None

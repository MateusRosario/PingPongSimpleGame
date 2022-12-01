from Point import Point
import pygame
from Estremidade import Estremidade

class Player:
    def __init__(self, player, cor, id_especial_1, id_especial_2, id_especial_3, estremidade, controle):
        self.posicao = Point(0, 0)
        self.id_1 = id_especial_1
        self.id_1_usado = False
        self.id_2 = id_especial_2
        self.id_2_usado = False
        self.id_3 = id_especial_3
        self.id_3_usado = False
        self.estrem = estremidade
        self.retang = None
        self.controle = controle
        self.v = 10
        self.cor = cor
        self.player = player
        self.movendo_dir = False
        self.movendo_esq = False

    def set_posicao(self, x, y):
        self.posicao.x = x
        self.posicao.y = y


    def mover(self, i):
        self.posicao.x = self.posicao.x + i
        if self.posicao.x - 30 < self.estrem.p1.x:
            self.posicao.x = self.estrem.p1.x + 30
        elif self.posicao.x + 30 > self.estrem.p2.x:
            self.posicao.x = self.estrem.p2.x - 30

    def get_evento(self, keys, especiais):
        for key in keys:
            if self.controle.dir(key):
                self.mover(self.v)
                self.movendo_dir = True
            else:
                self.movendo_dir = False
            if self.controle.esq(key):
                self.mover(-self.v)
                self.movendo_esq = True
            else:
                self.movendo_esq = False
            if self.controle.es1(key) and not self.id_1_usado:
                especiais.call(1, self.player)
                self.id_1_usado = True
            if self.controle.es2(key) and not self.id_2_usado:
                especiais.call(2, self.player)
                self.id_2_usado = True
            if self.controle.es3(key) and not self.id_3_usado:
                especiais.call(3, self.player)
                self.id_3_usado = True

    def draw(self, display):
        self.retang = pygame.draw.line(display, self.cor, [self.posicao.x-30, self.posicao.y], [self.posicao.x+30, self.posicao.y], 4)

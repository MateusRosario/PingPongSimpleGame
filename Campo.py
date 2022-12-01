import pygame
import math

class Campo:
    def __init__(self, estremidade_l, estremidade_r, estremidade_t, estremidade_b):
        self.es_l = estremidade_l
        self.es_r = estremidade_r
        self.es_t = estremidade_t
        self.es_b = estremidade_b

        self.ponto_medio_l = int(self.es_t.p1.x + (self.es_b.p1.x - self.es_t.p1.x) / 2), int(self.es_t.p1.y + (self.es_b.p1.y - self.es_t.p1.y) / 2)
        self.ponto_medio_r = int(self.es_t.p2.x + (self.es_b.p2.x - self.es_t.p2.x) / 2), int(self.es_t.p2.y + (self.es_b.p2.y - self.es_t.p2.y) / 2)
        self.meio_de_campo = int(self.ponto_medio_l[0] + (self.ponto_medio_r[0] - self.ponto_medio_l[0]) / 2), int(self.ponto_medio_l[1] + (self.ponto_medio_r[1] - self.ponto_medio_l[1]) / 2)

    def atingiu(self):
        pass

    def draw(self, display):
        tam_do_circulo = 60
        verde = [0,255,0]

        pygame.draw.line(display, verde, self.es_l.p1.get_list(), self.es_l.p2.get_list(), 2)
        pygame.draw.line(display, verde, self.es_r.p1.get_list(), self.es_r.p2.get_list(), 2)
        pygame.draw.line(display, verde, self.es_t.p1.get_list(), self.es_t.p2.get_list(), 2)
        pygame.draw.line(display, verde, self.es_b.p1.get_list(), self.es_b.p2.get_list(), 2)


        pygame.draw.line(display, verde, self.ponto_medio_l, self.ponto_medio_r, 2)


        area = [self.meio_de_campo[0] - tam_do_circulo, self.meio_de_campo[1] - tam_do_circulo, tam_do_circulo*2, tam_do_circulo*2]
        pygame.draw.arc(display, verde, area, 0, 2*math.pi, 2)

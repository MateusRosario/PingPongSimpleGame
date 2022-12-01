import pygame

class Bola:
    def __init__(self, tipo, vetor, campo):
        self.tipo = tipo
        self.vetor = vetor # lista com a velocidade x e y
        self.imagem = pygame.image.load("bola.png")
        self.imagem = pygame.transform.scale(self.imagem, [30, 30])
        self.bola = self.imagem.get_rect()

        self.vetory_foi_invertido = False

        if tipo == 1:
            self.set_posicao_inicial_centro(campo)

    def set_posicao_inicial_centro(self, campo):
        ponto_medio1 = int(campo.es_t.p1.x + (campo.es_b.p1.x - campo.es_t.p1.x) / 2), int(campo.es_t.p1.y + (campo.es_b.p1.y - campo.es_t.p1.y) / 2)
        ponto_medio2 = int(campo.es_t.p2.x + (campo.es_b.p2.x - campo.es_t.p2.x) / 2), int(campo.es_t.p2.y + (campo.es_b.p2.y - campo.es_t.p2.y) / 2)

        self.bola.center = int(ponto_medio1[0] + (ponto_medio2[0] - ponto_medio1[0]) / 2), int(ponto_medio1[1] + (ponto_medio2[1] - ponto_medio1[1]) / 2)

    def set_posicao_inicial(self, x, y):
        self.bola.center = x, y

    def get_posicao(self):
        return self.bola.center


    def draw(self, display, campo, player1_rec, player2_rec, especiais, partida):
        self.bola = self.bola.move(self.vetor)


        if campo.es_l.p1.x > self.bola.left:
            self.vetor[0] = -self.vetor[0]
        elif campo.es_r.p1.x < self.bola.right:
            self.vetor[0] = -self.vetor[0]


        if campo.es_t.p1.y >= self.bola.top:
            if campo.es_t.is_reflete():
                if not self.vetory_foi_invertido:
                    self.vetor[1] = -self.vetor[1]
                    self.vetory_foi_invertido = True
                    especiais.colisao_com_t()
                else:
                    self.vetory_foi_invertido = False
            else:
                partida.ponto_marcado(1)
            if self.tipo == 2:
                especiais.apagar_bolas_p1()
        elif campo.es_b.p1.y <= self.bola.bottom:
            if campo.es_b.is_reflete():
                if not self.vetory_foi_invertido:
                    self.vetor[1] = -self.vetor[1]
                    self.vetory_foi_invertido = True
                    especiais.colisao_com_b()
                else:
                    self.vetory_foi_invertido = False
            else:
                partida.ponto_marcado(2)
            if self.tipo == 2:
                especiais.apagar_bolas_p2()

        display.blit(self.imagem, self.bola)


        if self.bola.colliderect(player1_rec):
            if not self.vetory_foi_invertido:
                especiais.colisao_com_p1()
                self.vetor[1] = -self.vetor[1]
                self.vetory_foi_invertido = True
                if partida.player1.movendo_dir:
                    self.vetor[0] = self.vetor[0] + 1.5
                elif partida.player1.movendo_esq:
                    self.vetor[0] = self.vetor[0] - 1.5
                if self.vetor[0] > 10:
                    self.vetor[0] = 10
                elif self.vetor[0] < -10:
                    self.vetor[0] = -10
                if self.tipo == 2:
                    return -1
            else:
                self.vetory_foi_invertido = False

        if self.bola.colliderect(player2_rec):
            if not self.vetory_foi_invertido:
                especiais.colisao_com_p2()
                self.vetor[1] = -self.vetor[1]
                self.vetory_foi_invertido = True
                if partida.player2.movendo_dir:
                    self.vetor[0] = self.vetor[0] + 1.5
                elif partida.player2.movendo_esq:
                    self.vetor[0] = self.vetor[0] - 1.5
                if self.tipo == 2:
                    return -1
            else:
                self.vetory_foi_invertido = False
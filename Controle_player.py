class Controle_player:
    def __init__(self, esquerda, direita, especial1, especial2, especial3):
        self.direita = direita
        self.esquerda = esquerda
        self.especial1 = especial1
        self.especial2 = especial2
        self.especial3 = especial3

    def dir(self, key):
        return True if key == self.direita else False

    def esq(self, key):
        return True if key == self.esquerda else False

    def es1(self, key):
        return True if key == self.especial1 else False

    def es2(self, key):
        return True if key == self.especial2 else False

    def es3(self, key):
        return True if key == self.especial3 else False

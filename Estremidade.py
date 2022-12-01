class Estremidade:
    def __init__(self, p1, p2, reflete):
        self.p1 = p1
        self.p2 = p2
        self.reflete = reflete # diz se ao ato da bola atigingir esta estremidade, a bola bate e volta ou o jogador marca um ponto.

    def is_reflete(self):
        return True if self.reflete == "reflete" else False

    def get_points(self):
        return [self.p1.get_list(), self.p2.get_list()]
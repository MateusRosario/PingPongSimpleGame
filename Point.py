class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_list(self):
        return [self.x, self.y]
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def a(self):
        return self.x, self.y
v = Vector(2,3)
print(v.a())
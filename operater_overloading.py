class multi:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, z):
        x = self.x + z.x
        y = self.y + z.y
        return multi(x,y)

    def __str__(self):
        return "({0}),({1})".format(self.x, self.y)


m1 = multi(4, 2)
m2 = multi(3, 4)
print(m1 * m2)

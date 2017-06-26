class Points(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, b):
        return Points(self.x - b.x, self.y - b.y, self.z - b.z)

    def dot(self, b):
        return self.x * b.x + self.y * b.y + self.z * b.z

    def cross(self, b):
        return Points(self.y * b.z - self.z * b.y,
                      self.z * b.x - self.x * b.z,
                      self.x * b.y - self.y * b.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


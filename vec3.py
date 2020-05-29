import random


class vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        mag = (self.x**2 + self.y**2 + self.z**2)**0.5
        return vec3(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, n):
        return self.x*n.x + self.y*n.y + self.z*n.z  # Dot product

    def __mul__(self, number):
        return vec3(number*self.x, number*self.y, number*self.z)

    def __rmul__(self, lhs):
        return self * lhs  # Effectively, turn 7 * v into v * 7

    def __add__(self, vector3):
        return vec3(self.x+vector3.x, self.y+vector3.y, self.z+vector3.z)

    def __sub__(self, vector3):
        return vec3(self.x-vector3.x, self.y-vector3.y, self.z-vector3.z)


def random_vec3(n1=-1, n2=1):
    return vec3(random.uniform(n1, n2), random.uniform(n1, n2), random.uniform(n1, n2))

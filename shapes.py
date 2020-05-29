import numpy as np
from math import fabs
from vec3 import *


class Box:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.rectangles = [
            Rectangle(
                vec3(p1.x, p2.y, p1.z),
                vec3(p2.x, p1.y, p1.z)
            ),

            Rectangle(
                vec3(p1.x, p2.y, p2.z),
                vec3(p1.x, p1.y, p1.z)
            ),

            Rectangle(
                vec3(p1.x, p1.y, p1.z),
                vec3(p2.x, p1.y, p2.z)
            ),

            Rectangle(
                vec3(p1.x, p2.y, p2.z),
                vec3(p2.x, p1.y, p2.z)
            ),

            Rectangle(
                vec3(p2.x, p2.y, p2.z),
                vec3(p2.x, p1.y, p1.z)
            ),

            Rectangle(
                vec3(p1.x, p2.y, p1.z),
                vec3(p2.x, p2.y, p2.z)
            )
        ]

    def get2DRectangles(self, n, p):
        return [rect.get2D(n, p) for rect in self.rectangles]

    def isInBox(self, p):
        if p.x < min(self.p1.x, self.p2.x) or p.x > max(self.p1.x, self.p2.x):
            return False
        if p.y < min(self.p1.y, self.p2.y) or p.y > max(self.p1.y, self.p2.y):
            return False
        if p.z < min(self.p1.z, self.p2.z) or p.z > max(self.p1.z, self.p2.z):
            return False
        return True


class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get2D(self, n, p):
        p1 = project3D_on_2D(self.p1, n, p)
        p2 = project3D_on_2D(self.p2, n, p)
        return (p1.x, p1.y, fabs(p2.x-p1.x), fabs(p2.y-p1.y))


def project3D_on_2D(point3D, n, p):
    v = point3D-p
    perp_dist = v.dot(n)
    projected = point3D-perp_dist*n
    x = int(projected.x)
    y = int(projected.y)
    return vec3(x, y, 0)  # or just use projected if no integer casting


def almost_equal_pos(p1, p2, delta=5):
    # p1 = project3D_on_2D(p1, vec3(0, 0, 1), vec3(0, 0, 0))
    # p1 = vec3(p1.x, p1.y, 0)
    # p2 = project3D_on_2D(p2, vec3(0, 0, 1), vec3(0, 0, 0))
    # p2 = vec3(p2.x, p2.y, 0)
    if fabs(p1.x-p2.x) > delta:
        return False
    if fabs(p1.y-p2.y) > delta:
        return False
    if fabs(p1.z-p2.z) > delta:
        return False
    return True

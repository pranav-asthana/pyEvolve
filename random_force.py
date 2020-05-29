from vec3 import *


class RandomForce():
    def __init__(self):
        self.magnitude = random.uniform(0, 2)
        self.direction = random_vec3()

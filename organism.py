from random_force import *


class Organism:
    def __init__(self, position, velocity, gene_length):
        self.position = position
        self.velocity = velocity

        # # Used to show status: dead/alive/reached target
        # self.color = (0, 0, 0)

        self.fitness = 1
        self.alive = True
        self.success = False

        self.gene_length = gene_length
        self.gene = [RandomForce() for f in range(gene_length)]

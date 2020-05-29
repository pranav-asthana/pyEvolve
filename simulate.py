from organism import *
from random_force import *
from evolve import *
from shapes import *

import pygame
import numpy as np


class Simulation:
    def __init__(self, population_size, duration, generations, mutation_rate):
        self.population = population_size
        self.duration = duration
        self.generations = generations
        self.mutation_rate = mutation_rate

        self.organisms = []
        self.mating_pool = []

        self.birth_position = vec3(800, 850, 0)
        self.target = vec3(800, 100, 200)
        self.obstacles = [Box(vec3(500, 500, -200), vec3(1100, 400, 200))]

        pygame.init()
        self.screen = pygame.display.set_mode([1600, 900])

    def createPopulation(self):
        # Initial velocity is (0, 0, 0), depends on the forces applied
        # Gene length = number of forces applies = duration of one generation of the simulation
        self.organisms = [Organism(self.birth_position, vec3(0, 0, 0), self.duration)
                          for p in range(self.population)]

    def reset_organisms(self):
        for o in self.organisms:
            o.position = self.birth_position
            o.velocity = vec3(0, 0, 0)

    def move_organisms(self, iter):
        for o in self.organisms:
            force = o.gene[iter]
            o.velocity += force.magnitude * force.direction.normalize()
            o.position += o.velocity

            for box in self.obstacles:
                # print(o.position, box.isInBox(o.position))
                if box.isInBox(o.position):
                    o.alive = False

            if almost_equal_pos(o.position, self.target):
                o.success = True

    def draw_organisms(self, iter):

        # Provides an orthographic projection
        n = vec3(0, 0, 1)  # Normal to the plane
        p = vec3(0, 0, 0)  # Any point on the plane

        self.screen.fill((255, 255, 255))
        # Draw target
        target_2D = project3D_on_2D(self.target, n, p)
        target_2D = (target_2D.x, target_2D.y)

        pygame.draw.circle(self.screen, (0, 0, 0),
                           target_2D, 20)
        pygame.draw.circle(self.screen, (0, 255, 0),
                           target_2D, 15)
        pygame.draw.circle(self.screen, (255, 0, 0),
                           target_2D, 10)

        # Draw obstacles
        for o in self.obstacles:
            rects = o.get2DRectangles(n, p)
            for r in rects:
                pygame.draw.rect(self.screen, (100, 100, 100), r)

        # Rectangle((0, 0, 10), (100, 100, 10)).draw2D(n, p)

        # Draw organisms
        for o in self.organisms:
            color = (0, 0, 0)
            if not o.alive:
                color = (255, 0, 0)
                # continue
            if o.success and o.alive:
                color = (0, 255, 0)
            pos = project3D_on_2D(np.array(o.position), n, p)
            pygame.draw.circle(self.screen, color, (pos.x, pos.y), 5)

        pygame.display.flip()

    def simulate(self):
        self.createPopulation()
        gen = 1
        while gen <= self.generations:
            gen += 1
            iter = 0
            while (1):  # Simulation of 1 generation
                if iter == self.duration:
                    break

                self.draw_organisms(iter)
                self.move_organisms(iter)

                pygame.time.wait(10)
                iter += 1
            # Selection and mating
            mating_pool = select(self.organisms)
            self.organisms = mate(mating_pool)
            self.reset_organisms()
        pygame.quit()


def main():
    population_size = 1000
    duration = 100
    generations = 100
    mutation_rate = 0
    simulation = Simulation(population_size, duration,
                            generations, mutation_rate)
    simulation.simulate()


if __name__ == '__main__':
    main()


# Roulette wheel selection


def select(population):
    mating_pool = []

    max_fitness = max(o.fitness for o in population)
    avg_fitness = sum(o.fitness for o in population)/max_fitness

    print(avg_fitness)

    for o in population:
        normalized_fitness = o.fitness/max_fitness
        normalized_fitness *= 1000  # Arbitrary multiplier
        # Higher fitness will mean more of the same organism is added to the mating pool.
        # This is a way to give a higher mating probability to higher fitness
        for i in range(int(normalized_fitness)):
            mating_pool.append(o)

    return mating_pool


def mate(mating_pool):
    return mating_pool
    pass

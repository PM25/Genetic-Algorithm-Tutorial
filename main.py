#%%
import math
import numpy as np


weights_size = 3
count = 15

#%%
import math


def init_population():
    population_size = (count, weights_size)
    new_population = np.random.uniform(low=-4.0, high=4.0, size=population_size)
    return new_population


def fitness(individual):
    x, y, z = individual
    output = x ** 2 // y + math.exp(z)
    return output


def mutation():
    pass


def crossover():
    pass


def selection(population, top_proportion=0.5):
    individual_scores = []
    for individual in population:
        individual_scores.append((individual, fitness(individual)))
    sorted(individual_scores, key=lambda tup: tup[1])
    pool = individual_scores[: math.ceil(len(individual_scores) * top_proportion)]
    return pool


#%%
population = init_population()
print(population)

#%%
topfitness = selection(population, 0.5)
print(topfitness)

# %%

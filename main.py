#%%
import random
import math
import numpy as np


weights_size = 5
count = 15
max_iter = int(1e2)

#%%
# define a random function to solved
def fitness(individual):
    x = individual
    output = x[0] ** 2 // x[1] + math.exp(x[2]) - x[3]
    output += random.random()
    return output


def init_population(count, weights_size):
    population_size = (count, weights_size)
    new_population = np.random.uniform(low=-4.0, high=4.0, size=population_size)
    return new_population


def mutation(individual, prob=0.1):
    if random.random() < prob:
        idx = int(len(individual) * random.random())
        individual[idx] += random.random() * 2 - 1

    return individual


def crossover(parents, offspring_sz):
    children = []
    for idx in range(offspring_sz):
        if idx % len(parents) == 0:
            random.shuffle(parents)

        crossover_point = int(random.random() * len(parents[0]))
        p1, p2 = parents[idx % len(parents)], parents[(idx + 1) % len(parents)]
        child = p1[:crossover_point] + p2[crossover_point:]
        children.append(mutation(child))
    return children


def selection(population, top_proportion=0.5):
    individual_scores = []
    for individual in population:
        individual_scores.append((list(individual), fitness(individual)))
    individual_scores = sorted(individual_scores, key=lambda tup: tup[1], reverse=True)
    pool = individual_scores[: math.ceil(len(individual_scores) * top_proportion)]
    return pool


def mean(li):
    return sum(li) / len(li)


#%%
population = init_population(count, weights_size)
# print("-" * 5, "Init Population", "-" * 5)
# print(population)

scores = []
best_individual = None
for step in range(max_iter):
    topfitness_with_score = selection(population, 0.5)
    topfitness = [individual for individual, score in topfitness_with_score]
    best_individual = topfitness[0]
    avg_score = mean([score for individual, score in topfitness_with_score])
    scores.append(avg_score)

    offspring = crossover(topfitness, count)
    population = offspring

#%%
import matplotlib.pyplot as plt

plt.xlabel("epoch")
plt.ylabel("score")
plt.plot(scores)
print(f"Optimal Solution: {best_individual}")

#%%

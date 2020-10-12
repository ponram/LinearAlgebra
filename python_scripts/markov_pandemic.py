import numpy as np
import matplotlib.pyplot as plt

(h0, z0) = (135, 165) #initial population of humans and zombies
m = np.array([[0.8, 0.1],[0.2, 0.9]]) #markov matrix
human_pop = []
zombie_pop = []
pop = np.array([[h0],[z0]])

for t in range(100):
    pop = np.dot(m,pop)
    human_pop_t = int(np.round(pop[0]))
    zombie_pop_t = int(np.round(pop[1]))
    human_pop.append(human_pop_t)
    zombie_pop.append(zombie_pop_t)

plt.plot(human_pop, zombie_pop)

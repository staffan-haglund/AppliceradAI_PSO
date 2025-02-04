import random
import sys
import numpy as np
import matplotlib.pyplot as plt

from math import cos, pi

class PSO:
    """
    A class to represent a swarm for PSO.

    Attributes
    ----------
    swarm_size : int
        Nr of particles
    dimensions : int
        Nr of dimensions
    max_iter : int
        Max nr of iterations
    w : float
        Inertia weight
    c1 : float
        Cognitive coefficient
    c2 : float
        Social coefficient
    xmin : float
        Lower boundary
    xmax : float
        Upper boundary
    rand_seed : int
        Seed for random generation\n
        Default=42
    func : str
        Optimisation function. Possible values: 'Rastrigin' or 'Sphere'.\n
        Default='Rastrigin'

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, swarm_size: int, dimensions: int, max_iter: int, 
                 w=0.7, c1=2.0, c2=2.0, xmin=-5.12, xmax=5.12, rand_seed=42, func='Rastrigin'):
        self._swarm_size = swarm_size       # Antal partiklar
        self._dimensions = dimensions       # Antal dimensioner
        self._max_iter = max_iter
        self._w = w                         # Inertia weight
        self._c1 = c1                       # Cognitive coefficient
        self._c2 = c2                       # Social coefficient
        self._xmin = xmin
        self._xmax = xmax
        self._func = func
        self._swarm = {}
        random.seed(rand_seed)
        for i in range(self._swarm_size):
            self._swarm[i] = {'Position': [round(random.uniform(self._xmin, self._xmax), 2) for x in range(self._dimensions)], \
                              'Velocity': [round(random.uniform(self._xmin, self._xmax), 2) for v in range(self._dimensions)]}
        temp_pbest_value = 0.0
        for i in range(self._swarm_size):
            self._swarm[i]['pbest'] = self._swarm[i]['Position']
            self._swarm[i]['best_value'] = self.rastrigin_fitness(self._swarm[i]['Position'])
            # Om nytt personbästa (pbest) är bättre än temp_pbest, 
            # spara pbest som ny global bästa (gbest)
            # spara ny pbest som ny temp_pbest
            if abs(self._swarm[i]['best_value']) < abs(temp_pbest_value):
                self._swarm['gbest'] = self._swarm[i]['pbest']
                temp_pbest_value = self._swarm[i]['best_value']
            # Annars, behåll bästa pbest som gbest
            else:
                self._swarm['gbest'] = self._swarm[i]['pbest']
        
        # Spara gbest_value från den med gbest position
        self._swarm['gbest_value'] = self.rastrigin_fitness(self._swarm['gbest'])

        for i in range(self._swarm_size):
            self._swarm[i]['Fitness'] = self.rastrigin_fitness(self._swarm[i]['Position'])


    def __str__(self):
        str_info = [f'{self._swarm[particle]}\n' for particle in self._swarm]
        return str(''.join(str_info))


    def get_swarm(self) -> dict:
        return self._swarm
    

    def get_swarm_specs(self):
        return {'Size': self._swarm_size, 'Dimensions': self._dimensions, 'Max iterations': self._max_iter, 
                'Inertia weight': self._w, 'Cognitive coefficient': self._c1, 'Social coefficient': self._c2, 
                'Search domain': (self._xmin, self._xmin), 'Function': self._func}
    

    def get_particle(self):
        print("-----------------------------------")
        for i in range(self._swarm_size):
            print(f'Particle #{i}: Position: {self._swarm[i]['Position']} | pbest: {self._swarm[i]['pbest']} | gbest: {self._swarm['gbest']}')
        # return self._swarm[i]

    def sphere_fitness(self, particle):
        fitness = sum((x ** 2) for x in particle)
        return fitness


    def rastrigin_fitness(self, particle):
        fitness = 10 * self._dimensions + sum((x ** 2) - 10 * cos(2 * pi * x) for x in particle)
        return fitness
        

    def update_swarm(self):
        print("-----------------------------------")
        print("UPDATE SWARM")
        for iteration in range(self._max_iter):
            # print(f'Iteration #{iteration}')
            for i in range(self._swarm_size):
                # Utvärdera nuvarande position
                current_value = self.rastrigin_fitness(self._swarm[i]['Position'])
                # Uppdatera personbästa
                if current_value < self._swarm[i]['best_value']:
                    self._swarm[i]['pbest'] = self._swarm[i]['Position']
                    self._swarm[i]['best_value'] = current_value
                #  Uppdatera globalt bästa
                if current_value < self._swarm['gbest_value']:
                    self._swarm['gbest'] = self._swarm[i]['Position']
                    self._swarm['gbest_value'] = current_value

            for i in range(self._swarm_size):
                r1 = round(random.random(), 3)
                r2 = round(random.random(), 3)

                # Hastighetsuppdatering
                v_new = []
                for j in range(self._dimensions):
                    v_new.append(self._w * self._swarm[i]['Velocity'][j] + \
                        self._c1 * r1 * (self._swarm[i]['pbest'][j] - self._swarm[i]['Position'][j]) + \
                            self._c2 * r2 * (self._swarm['gbest'][j] - self._swarm[i]['Position'][j]))
                self._swarm[i]['Velocity'] = v_new
                # Positionsuppdatering
                p_new = []
                for k in range(self._dimensions):
                    # particles[i].x = particles[i].x + particles[i].v
                    p_new.append(self._swarm[i]['Position'][k] + self._swarm[i]['Velocity'][k])
                self._swarm[i]['Position'] = p_new

    def plot_convergence(self):
        plt.figure(figsize=(8, 5))
        plt.plot(self._max_iter, best_fitness_values, marker='o', linestyle='-', color='b', label="Best fitness")

        plt.xlabel("Iterationer")
        plt.ylabel("Best Fitness Value")
        plt.title("PSO Konvergenskurva")
        plt.legend()
        plt.grid()

        plt.show()

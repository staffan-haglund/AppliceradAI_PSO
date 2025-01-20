import random
import sys
import numpy as np

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
                              'Velocity': round(random.uniform(self._xmin, self._xmax), 2)}
        for i in range(self._swarm_size):
            self._swarm[i]['pbest'] = self._swarm[i]['Position']

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
    
    def sphere_fitness(self, particle):
        fitness = sum((x ** 2) for x in particle)
        return fitness

    def rastrigin_fitness(self, particle):
        # for i in range(len(particle)):
        #     print(f'i: {particle[i]}')
        fitness = 10 * self._dimensions + sum((x ** 2) - 10 * cos(2 * pi * x) for x in particle)
        return fitness
        

    def update_particle(self):
        for i in range(self._swarm_size):
            # print(f'{self._swarm[i]['Position']}')  # = {'Velocity': round(random.uniform(self._xmin, self._xmax), 2)}
            self.rastrigin_fitness(self._swarm[i]['Position'])
        # r1 = round(random.random(), 3)
        # r2 = round(random.random(), 3)
        # # Update velocity
        # vi​=w⋅vi​+c1​⋅r1​⋅(pi​−xi​)+c2​⋅r2​⋅(g−xi​)

    
from pso import PSO



if __name__ == "__main__":

    new_swarm = PSO(swarm_size=5, dimensions=2, max_iter=100, rand_seed=3)
    print(str(new_swarm))

    print(new_swarm.get_swarm_specs())
    print(new_swarm.get_swarm())
    print("\nSTART ###############################################")
    print(f'Antal iterationer: {new_swarm._max_iter}')

    new_swarm.get_particle()
    new_swarm.update_swarm()
    new_swarm.get_particle()

    # print(f'Particle #0: {new_swarm.get_particle(0)}')
    
    # new_swarm.update_particle()

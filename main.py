from pso import PSO



if __name__ == "__main__":

    new_swarm = PSO(swarm_size=5, dimensions=2, max_iter=100)
    print(str(new_swarm))

    print(new_swarm.get_swarm_specs())

    print(new_swarm.get_swarm())

    new_swarm.update_particle()

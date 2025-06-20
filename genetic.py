import pygad, numpy, os
from main import mainProgram

inputs = [1.0, 0.0,
          0.4, 10.0, 0.8, -0.1,
          0.2, 20.0, 1.1, -0.3
          ]
liftCoefficient = 0.0

def fitnessFunction(ga_instance, solution, solution_idx):
    global liftCoefficient
    #print("Current Best Fitness:", ga_instance.best_solutions_fitness)
    liftCoefficient = mainProgram(solution)
    fitness = liftCoefficient
    #print("Current Fitness:", fitness)
    return fitness
    
def on_start(ga_instance):
    global liftCoefficient
    liftCoefficient = mainProgram(inputs)

#def on_generation(ga_instance):
    #global liftCoefficient
    #mutatedInputs = ga_instance.best_solution()[0]
    #liftCoefficient = mainProgram(mutatedInputs)
    
myFitnessFunction = fitnessFunction
myOnStartFunction = on_start
#myOnGenerationFunction = on_generation
    
numGenerations = 10
numParentsMating = 15
solPerPop = 30
numGenes = len(inputs)

ga_instance = pygad.GA(num_generations=numGenerations,
                        num_parents_mating=numParentsMating,
                        sol_per_pop=solPerPop,
                        num_genes=numGenes,
                        fitness_func=myFitnessFunction,
                        #on_generation=myOnGenerationFunction,
                        on_start=myOnStartFunction,
                        save_solutions=True,
                        save_best_solutions=True,
                        gene_space=[1.0, 0.0,
                                    numpy.arange(0.40, 0.50, 0.02), numpy.arange(10.0, 15.0, 0.5), 0.8, numpy.arange(-0.12, -0.15, -0.01),
                                    numpy.arange(0.15, 0.20, 0.01), numpy.arange(20.0, 30.0, 0.5), 1.2, numpy.arange(-0.18, -0.30, -0.01)
                                    ])
ga_instance.run()
ga_instance.plot_fitness()
import pygad, numpy, os
from main import mainProgram

inputs = [1.0, 0.0,                 #element 1 scale and AoA
          0.3, 7.0, 0.8, -0.07     #element 2 scale, AoA, x-position, y-position
          #0.2, 10.0, 1.1, -0.19     #element 3 scale, AoA, x-position, y-position
          ]
liftCoefficient = 0.0               #initializing variable to store current lift coefficient

def fitnessFunction(ga_instance, solution, solution_idx):
    global liftCoefficient
    #print("Current Best Fitness:", ga_instance.best_solutions_fitness)
    liftCoefficient = mainProgram(solution)
    fitness = liftCoefficient
    print("Current Fitness:", fitness)
    return fitness
    
def on_start(ga_instance):
    global liftCoefficient
    liftCoefficient = mainProgram(inputs)   #give inputs to main.py

#def on_generation(ga_instance):
    #global liftCoefficient
    #mutatedInputs = ga_instance.best_solution()[0]
    #liftCoefficient = mainProgram(mutatedInputs)
    
myFitnessFunction = fitnessFunction
myOnStartFunction = on_start
#myOnGenerationFunction = on_generation
    
numGenerations = 1
numParentsMating = 4
solPerPop = 5
numGenes = len(inputs)

#instance of GA is created
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
                                    numpy.arange(0.15, 0.30, 0.02), numpy.arange(3, 13, 0.5), 0.8, numpy.arange(-0.07, -0.10, -0.01)
                                    #numpy.arange(0.20, 0.25, 0.01), numpy.arange(13, 15, 0.5), 1.1, numpy.arange(-0.18, -0.21, -0.01)
                                    ])
#start running the GA
ga_instance.run()
ga_instance.plot_fitness()
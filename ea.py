import random
from classes.factory import Factory
from classes.population import Population
from classes.individual import Individual
from classes.operators import Operators as op

class EA:

    def __init__(self, factory: Factory, pop_size:int, n_gen:int, px:float, pm:float, tour_size:int):

        self.factory = factory
        self.pop_size = pop_size
        self.n_gen = n_gen
        self.px = px
        self.pm = pm
        self.tour_size = tour_size

        self.population = None
        self.best_indiv = None

    def run(self) -> Individual:
        """
        Main loop which creates a log with the information.
        Pseudocode 2 implemented
        """
        # Initialized the first Population
        factory = self.factory 
        self.population = Population(self.pop_size, factory.n_jobs, factory )
        self.best_indiv = self.population.best_individual

        # Opens a file and writes the data of the running on it
        with open(f"data/EA_{factory.name}.csv", "w") as f:
            f.write("generation,best,avg,worst\n")

            # Start a loop for performing all the generations
            for i in range(self.n_gen):
                new_individuals = []

                # Each loop creates a new Individual 
                while len(new_individuals) < self.pop_size:
                    # Selects from a "tournament" the best two in them
                    ind1 = self.population.tournament(self.tour_size)
                    ind2 = self.population.tournament(self.tour_size)

                    # If it complies a crossover is performed
                    if random.random() < self.px:
                        child = op.pmx(ind1, ind2)
                    else:
                        child = ind1.copy()
                    
                    # If it complies a mutation is performed
                    if random.random() < self.pm:
                        child = op.inversion(child)
                    
                    # Sees if the child is the best at the moment
                    child.evaluate(factory)
                    if child.fitness <= self.best_indiv.fitness:
                        self.best_indiv = child
                    
                    # Adds it to the new population
                    new_individuals.append(child)

                # Saves the new population
                self.population.individuals = new_individuals
                #Logs the data of the generation
                self._log(i, f)

        return self.best_indiv


    def _log(self, generation, f):
        fitnesses = [ind.fitness for ind in self.population.individuals]

        best = min(fitnesses)
        avg = sum(fitnesses) / len(fitnesses)
        worst = max(fitnesses)

        # This saves the data on the file opened
        f.write(f"{generation},{best},{avg:.2f},{worst}\n")


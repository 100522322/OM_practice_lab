import random
from factory import Factory
from population import Population
from individual import Individual
from operators import Operators as op

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
        factory = self.factory 
        self.population = Population(self.pop_size, factory.n_jobs, factory )
        self.best_indiv = self.population.best_individual

        # Opens a file and writes the data of the running on it
        with open(f"{factory.name}.csv", "w") as f:
            f.write("generation,best,avg,worst\n")

            for i in range(self.n_gen):
                new_individuals = []

                while len(new_individuals) < self.pop_size:
                    ind1 = self.population.tournament(self.tour_size)
                    ind2 = self.population.tournament(self.tour_size)

                    if random.random() < self.px:
                        child = op.ox(ind1, ind2)
                    else:
                        child = ind1.copy()
                    
                    if random.random() < self.pm:
                        child = op.inversion(child)
                    
                    child.evaluate(factory)
                    if child.fitness <= self.best_indiv.fitness:
                        self.best_indiv = child
                    
                    new_individuals.append(child)

                self.population.individuals = new_individuals
                self._log(i, f)

        return self.best_indiv


    def _log(self, generation, f):
        fitnesses = [ind.fitness for ind in self.population.individuals]

        best = min(fitnesses)
        avg = sum(fitnesses) / len(fitnesses)
        worst = max(fitnesses)

        # This saves the data on the file opened
        f.write(f"{generation},{best},{avg:.2f},{worst}\n")


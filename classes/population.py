from classes.individual import Individual
import random

class Population:

    def __init__(self, n_individuals, n_jobs, factory):
        self.factory = factory
        self.individuals = [Individual.random(n_jobs) for _ in range(n_individuals)]

        self.evaluate_individuals()

        self.best_individual = min(self.individuals)
    

    def evaluate_individuals(self):
        """
        Evaluate all individuals on the Population which dont have a fitness
        """
        for ind in self.individuals:
            if ind.fitness is None:
                ind.evaluate(self.factory)

    def tournament(self, t_size):
        """
        From a random sample of size: t_size, returns the best Individual
        """
        ind_sample = random.sample(self.individuals, t_size)
        return min(ind_sample)
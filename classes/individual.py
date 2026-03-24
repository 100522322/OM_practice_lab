from classes.factory import Factory
import random

class Individual:
    """
    Class for evaluating an individual solution
    """
    def __init__(self, sequence):
        self.sequence = sequence
        self.fitness = None
    
    def evaluate(self, factory: Factory):
        """Evaluates the time it takes to complete sequence"""
        self.fitness = factory.evaluate(self.sequence)

    def copy(self) -> "Individual":
        """Creates a copy of the individual"""
        new_ind = Individual(list(self.sequence))
        new_ind.fitness = self.fitness
        return new_ind

    @classmethod
    def random(cls, n_jobs: int) -> "Individual":
        """Creates and individual with random sequence"""
        seq = list(range(n_jobs))
        random.shuffle(seq)
        return cls(seq)

    def __gt__(self, other):
        return self.fitness > other.fitness
    
    def __eq__(self, other):
        return self.fitness == other.fitness
        
import random
from classes.individual import Individual

class Operators:
    
    @staticmethod
    def swap(individual: Individual):
        """
        select randomly 2 indexes, Swap their position
        """
        ind = individual.copy()
        seq = ind.sequence
        
        # Selects 2 random indexes
        idx1, idx2 = random.sample(range(len(seq)), 2)
        # changes the values on those indexes
        seq[idx1], seq[idx2] = seq[idx2], seq[idx1]

        ind.sequence = seq
        ind.fitness = None
        return ind
    
    @staticmethod
    def inversion(individual: Individual):
        """
        Select randomly 2 indexes, then inverses the sequence between them
        """
        ind = individual.copy()
        seq = ind.sequence

        # Selects 2 random indexes
        idx1, idx2 = sorted(random.sample(range(len(seq)), 2))

        seq[idx1:idx2+1] = seq[idx1:idx2+1][::-1]

        ind.sequence = seq
        ind.fitness = None
        return ind
    
    @staticmethod
    def ox(parent1: Individual, parent2: Individual):
        """
        Ordered Crossover
        Select random segment of P1
        Insert on same segment of offspring
        Insert by order the jobs of P2 without repeating
        """
        p1_seq = parent1.sequence
        p2_seq = parent2.sequence
        size = len(p1_seq)

        # Pick 2 cut points
        idx1, idx2 = sorted(random.sample(range(size), 2))

        # Copy segment from parent1
        offspring_seq = [None] * size
        segment = p1_seq[idx1:idx2+1]
    
        offspring_seq[idx1:idx2+1] = segment
        segment_set = set(segment) 


        # Fill rest from parent2 in order, skipping duplicates
        p2_pointer = 0
        for i in range(size):
            if idx1 <= i <= idx2:
                continue
                
            # See if it was already in
            while p2_seq[p2_pointer] in segment_set:
                p2_pointer += 1
                
            offspring_seq[i] = p2_seq[p2_pointer]
            p2_pointer += 1

        # Reset fitness, return offspring
        offspring = parent1.copy()
        offspring.sequence = offspring_seq
        offspring.fitness = None
        return offspring

    @staticmethod
    def pmx():
        pass

    @staticmethod
    def cx():
        pass
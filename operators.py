import random


class Operators:
    
    @staticmethod
    def swap(individual):
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
    def inversion(individual):
        ind = individual.copy()
        seq = ind.sequence

        # Selects 2 random indexes
        idx1, idx2 = random.sample(range(len(seq)), 2)
        if idx1 > idx2:
            idx1,  idx2 = idx2, idx1

        seq[idx1:idx2] = seq[idx1:idx2][::-1]

        ind.sequence = seq
        ind.fitness = None
        return ind
    
    @staticmethod
    def ox(parent1, parent2):
        # 1. copy parent1
        # 2. pick 2 cut points
        # 3. copy segment from parent1
        # 4. fill rest from parent2 in order, skipping duplicates
        # 5. reset fitness, return offspring
        pass
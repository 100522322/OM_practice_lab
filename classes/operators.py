import random
from classes.individual import Individual

class Operators:
    
    @staticmethod
    def swap(individual: Individual, i1=None, i2=None) -> Individual:
        """
        select randomly 2 indexes, Swap their position
        """
        ind = individual.copy()
        seq = ind.sequence
        
        # Selects 2 random indexes
        if i1 is None or i2 is None:
            idx1, idx2 = random.sample(range(len(seq)), 2)
        else:
            idx1, idx2 = i1, i2
        # changes the values on those indexes
        seq[idx1], seq[idx2] = seq[idx2], seq[idx1]

        ind.sequence = seq
        ind.fitness = None
        return ind
    
    @staticmethod
    def inversion(individual: Individual) -> Individual:
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
    def ox(parent1: Individual, parent2: Individual) -> Individual:
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
    def pmx(p1: Individual, p2: Individual) -> Individual:
        """
        Partially Matched Crossover
        """
        p1_seq = p1.sequence
        p2_seq = p2.sequence
        size = len(p1_seq)

        # Picks 2 cut points
        idx1, idx2 = sorted(random.sample(range(size), 2))

        # maps the values of p1 into p2 segement values
        mapping = {}
        for a, b in zip(p1_seq[idx1:idx2+1], p2_seq[idx1:idx2+1]):
            mapping[a] = b
        
        # Makes a copy of p2_seq
        o1_seq = p2_seq[:]
        # Insert p1 segment into it
        o1_seq[idx1:idx2+1] = p1_seq[idx1:idx2+1]

        # Replace the duplicates
        for i in range(size):
            if idx1 <= i <= idx2:
                continue
            
            val = o1_seq[i]
            while val in p1_seq[idx1:idx2+1]:
                val = mapping[val]
            
            o1_seq[i] = val

        # Creates the individual
        o1 = p1.copy()
        o1.sequence = o1_seq
        o1.fitness = None
        return o1

    @staticmethod
    def cx():
        pass
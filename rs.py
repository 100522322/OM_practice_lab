from classes.individual import Individual
from classes.factory import Factory

class RandomSearch:

    def __init__(self, factory:Factory, n_evaluations):
        self.factory = factory
        self.n_evaluations = n_evaluations
        self.best_indiv = None
    
    def run(self):
        fact = self.factory
        jobs = fact.n_jobs
        
        with open(f"data/RS_{fact.name}.csv", "w") as f:
            f.write("generation,best,actual,worst\n")

            worst_fitness = 0
            # Try randomly to find the best solution
            for i in range(self.n_evaluations):
                ind = Individual.random(jobs)
                ind.evaluate(fact)

                if self.best_indiv is None or ind.fitness < self.best_indiv.fitness:
                    self.best_indiv = ind
                
                if worst_fitness < ind.fitness:
                    worst_fitness = ind.fitness
                
                f.write(f"{i},{self.best_indiv.fitness},{ind.fitness},{worst_fitness}\n")
        
        return self.best_indiv

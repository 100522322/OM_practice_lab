from classes.individual import Individual
from classes.factory import Factory

class RandomSearch:

    def __init__(self, factory:Factory, n_evaluations, pop_size):
        self.factory = factory
        self.n_evaluations = n_evaluations
        self.pop_size = pop_size
        self.best_indiv = None
    
    def run(self):
        fact = self.factory
        jobs = fact.n_jobs
        pop_size = self.pop_size
        with open(f"data/RS_{fact.name}.csv", "w") as f:
            f.write("generation,best,average,worst\n")

            window = []
            # Try randomly to find the best solution
            for i in range(self.n_evaluations):
                ind = Individual.random(jobs)
                ind.evaluate(fact)
                window.append(ind.fitness)

                if self.best_indiv is None or ind.fitness < self.best_indiv.fitness:
                    self.best_indiv = ind

                # Only  writes every pop_size for comparing with EA
                if i % pop_size == pop_size - 1:
                    avg = sum(window) / len(window)
                    worst = max(window)
                    generation = i  // pop_size
                    f.write(f"{generation},{self.best_indiv.fitness},{avg:.2f},{worst}\n")
                    window = []
        
        return self.best_indiv

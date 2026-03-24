from classes.factory import Factory
from classes.individual import Individual

class Greedy:
    def __init__(self, factory:Factory):
        self.factory = factory
        self.best_indiv = None

    def run(self):
        fact = self.factory
        n_jobs = fact.n_jobs

        jobs = list(range(n_jobs))
        final_sequence = []

        with open(f"data/Greedy_{fact.name}.csv", "w") as f:
            f.write("generation,best_next\n")

            # Repeat this until final sequence is completed
            i=0
            while len(final_sequence) != n_jobs:
                best = None
                best_time = None

                # Checks what job perform best in the evaluation
                for job in jobs:
                    time = fact.evaluate(final_sequence + [job])

                    if best is None or time < best_time:
                        best = job
                        best_time = time
            
                
                final_sequence.append(best)
                jobs.remove(best)

                f.write(f"{i},{best}\n")
                i += 1
        
        ind = Individual(final_sequence)
        ind.evaluate(fact)
        self.best_indiv = ind

        return ind





        


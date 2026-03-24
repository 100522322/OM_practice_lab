from classes.individual import Individual
from classes.factory import Factory
from classes.operators import Operators as op

class TabuSearch:

    def __init__(self, factory:Factory, n_iterations, tabu_size):
        self.factory = factory
        self.n_iterations = n_iterations
        self.tabu_size = tabu_size
        self.best_indiv = None
    
    def run(self):
        """
        Uses a Random individual to start
        Then search through its neightbours
        """
        fact = self.factory
        n_jobs = fact.n_jobs

        tabu_list = []

        ind = Individual.random(n_jobs)
        ind.evaluate(fact)
        self.best_indiv = ind

        with open(f"data/TabuSearch_{fact.name}.csv", "w") as f:
            f.write("generation,Best_general,Best_neighbour\n")


            for n in range(self.n_iterations):
                neighbours = []
                moves = []

                # Creates the neighbours and appends them
                for i in range(n_jobs):
                    # Swaps only different positions and no repetition
                    for j in range(i+1, n_jobs):
                        neigh = op.swap(ind, i, j)
                        neigh.evaluate(fact)
                        neighbours.append(neigh)

                        moves.append((i,j))
                

                best_neighbour = None
                best_move = None

                # Searches for the best neighbour and saves it
                for (i, j), neighbour in zip(moves, neighbours):
                    if (i, j) not in tabu_list:
                        if best_neighbour is None or neighbour.fitness < best_neighbour.fitness:
                            best_neighbour = neighbour
                            best_move = (i, j)
                
                # If all possible are Tabu
                if best_neighbour is None:
                    f.write(f"{n},{self.best_indiv.fitness},None\n")
                    continue

                # Updats tabu list
                tabu_list.append(best_move)
                if len(tabu_list) > self.tabu_size:
                    tabu_list.pop(0)
                
                # Updates best indiv if needed
                ind = best_neighbour
                if ind.fitness < self.best_indiv.fitness:
                    self.best_indiv = ind

                f.write(f"{n},{self.best_indiv.fitness},{best_neighbour.fitness}\n")


        return self.best_indiv



                    
 
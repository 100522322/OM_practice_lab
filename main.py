from classes.factory import Factory
from ea import EA
from rs import RandomSearch
from greedy import Greedy
from tabu_search import TabuSearch

# Load instance
factory = Factory()
factory.load_data("instances/tai20_5_0.fsp")
# print(factory)

# Parameters
pop_size = 100
n_gen = 100
px = 0.7
pm = 0.1
tour_size = 5

tabu_size = 10
n_iterations = n_gen

n_eval = pop_size * n_gen

ea = EA(
    factory=factory,
    pop_size=pop_size,
    n_gen=n_gen,
    px=px,
    pm=pm,
    tour_size=tour_size
)

rs = RandomSearch(
    factory=factory,
    n_evaluations=n_eval,
    pop_size=pop_size
)

greedy = Greedy(
    factory=factory
)

ts = TabuSearch(
    factory=factory,
    n_iterations=n_iterations,
    tabu_size=tabu_size
)

# Run Evolutionary Algorithm
best_ea = ea.run()
print(f"Best fitness found in EA: {best_ea.fitness}")
# print(f"Best sequence: {best.sequence}")

# Run Random Search
best_rs = rs.run()
print(f"Best fitness found in RS: {best_rs.fitness}")

# Greedy Algorithm
best_greedy = greedy.run()
print(f"Best fitness found in Greedy: {best_greedy.fitness}")

# Tabu Search
best_ts = ts.run()
print(f"Best fitness found in TabuSearch: {best_ts.fitness}")
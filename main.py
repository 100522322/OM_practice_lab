from classes.factory import Factory
from ea import EA
from rs import RandomSearch
from greedy import Greedy

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
    n_evaluations=n_eval
)

greedy = Greedy(
    factory=factory
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
from factory import Factory
from ea import EA

# Load instance
factory = Factory()
factory.load_data("instances/tai20_5_0.fsp")
print(factory)

# Running EA with "hints" from pdf
ea = EA(
    factory=factory,
    pop_size=100,
    n_gen=100,
    px=0.7,
    pm=0.1,
    tour_size=5
)

best = ea.run()
print(f"Best fitness found: {best.fitness}")
print(f"Best sequence: {best.sequence}")

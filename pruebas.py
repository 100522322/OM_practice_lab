fp = "instances/tai20_5_0.fsp"

with open(fp, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

p_times = []
for i, line in enumerate(lines):
    tokens = line.split()

    print(line)
    # Cheks the Jobs and Machines lines
    if i==1 and len(tokens) >= 2 and tokens[0].isdigit() and tokens[1].isdigit():
        j, m = int(tokens[0]), int(tokens[1])

        seed = int(tokens[2]) if tokens[2].isdigit() else None
        upper = int(tokens[3]) if tokens[3].isdigit() else None
        lower = int(tokens[4]) if tokens[4].isdigit() else None
    
    if i>=3:
        tokens = line.split()
        p_times.append(tokens)
    

print("-------------------")
print(len(p_times))
print(len(p_times[0]))
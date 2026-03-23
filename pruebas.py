import random


p1_seq = [1,2,3,4,5,6,7,8,9]
p2_seq = [5,7,4,9,1,3,6,2,8]
size = len(p1_seq)

# Pick 2 cut points
idx1, idx2 = 2, 5

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

print(offspring_seq)
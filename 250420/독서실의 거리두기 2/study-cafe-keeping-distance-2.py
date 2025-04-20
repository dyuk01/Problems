n = int(input())
seats = input()

# Please write your code here.
occupied = []
for idx, s in enumerate(seats): 
    if s == '1':
        occupied.append(idx)

# print(occupied)

open_distances = []
closed_distances = []
# 0 4 7 11

# Case1: Beginnig Empty
if occupied[0] != 0:
    open_distances.append(occupied[0])

i, j = 0, 1
while j < len(occupied):
    closed_distances.append(occupied[j] - occupied[i])
    i += 1
    j += 1

# Case2: End Empty
if occupied[-1] != n - 1:
    open_distances.append(n - 1 - occupied[-1])

new_closed_distances = []
for dist in closed_distances:
    new_closed_distances.append(dist // 2)

print(max(max(open_distances), max(new_closed_distances)))
n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Collect all movements in (x1, x2) format.
curr_pos = 0
movements = []
for pos, direct in zip(x, dir):
    if direct == "L":
        pos *= -1
        movements.append((curr_pos + pos, curr_pos))
    else:
        movements.append((curr_pos, curr_pos + pos))
    curr_pos += pos

# Find min and max to create overlap array.
min_x, max_x = float('inf'), 0
for x1, x2 in movements:
    if x1 < min_x:
        min_x = x1
    if x2 > max_x:
        max_x = x2

# Iterate through the movements and find overlaps.
overlaps = [0 for _ in range(min_x, max_x + 1)]
for x1, x2 in movements:
    if min_x < 0:
        x1 += (min_x * -1)
        x2 += (min_x * -1)
    else:
        x1 += min_x
        x2 += min_x
    # Exclude the last iteration for overlap.
    for i in range(x1, x2): 
        overlaps[i] += 1

# Add the number of overlaps in the array
res = 0
for overlap in overlaps:
    if overlap >= 2:
        res += 1

print(res)
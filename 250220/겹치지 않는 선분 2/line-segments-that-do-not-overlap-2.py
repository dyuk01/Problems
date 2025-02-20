n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines_sorted = sorted(lines, key=lambda x:x[0])

# Logic : as long as the next line doesn't end before the previous line,
# Lines do not overlap

# Return the number of non-overlapping lines

overlap = 0
for i in range(n):
    pivot_start_x, pivot_end_x = lines[i]
    for j in range(n):
        if i == j:
            continue
        
        curr_start_x, curr_end_x = lines[j]

        if (curr_start_x < pivot_start_x and curr_end_x > pivot_end_x) or (curr_start_x > pivot_start_x and curr_end_x < pivot_end_x):
            overlap += 1
print(overlap)


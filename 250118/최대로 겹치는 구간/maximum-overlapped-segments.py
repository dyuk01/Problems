n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

min_x, max_x = float('inf'), 0

# Find the active region of segments.
for x1, x2 in segments:
    if x1 < min_x:
        min_x = x1
    if x2 > max_x:
        max_x = x2

# 0-index the segment numbers.
# Then, mark overlap
overlaps = [0 for _ in range(min_x, max_x + 1)]
for x1, x2 in segments:
    for i in range(x1 - min_x, x2 - min_x + 1):
        overlaps[i] += 1

res = 0
for overlap in overlaps:
    if overlap > res:
        res = overlap

print(res)

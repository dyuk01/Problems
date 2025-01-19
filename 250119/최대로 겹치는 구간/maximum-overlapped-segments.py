n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# min_x, max_x = float('inf'), 0

# # Find the active region of segments.
# for x1, x2 in segments:
#     if x1 < min_x:
#         min_x = x1
#     if x2 > max_x:
#         max_x = x2

# overlaps = [0 for _ in range(min_x, max_x + 1)]
# # 0-index the segment numbers. (Normalize)
# for x1, x2 in segments:
#     if min_x < 0:
#         x1 += (min_x) * -1
#         x2 += (min_x) * -1
#     else:
#         x1 -= min_x
#         x2 -= min_x

#     # Iterate through overlaps.    
#     for i in range(x1, x2):
#         overlaps[i] += 1

# res = 0
# for overlap in overlaps:
#     if overlap > res:
#         res = overlap

# print(res)





# Split segments into unit intervals. (unit : x2 - x1 = 1)
# Segment coverage = x1 index increment 1.

# Initialize dict
counter = {}
for i in range(-100, 100):
    counter[i] = 0

# Itereate segments
for x1, x2 in segments:
    # Increment index based on interval
    for i in range(x1, x2):
        counter[i] += 1

# Find max
max_counter = 0
for val in counter.values():
    if val > max_counter:
        max_counter = val

print(max_counter)
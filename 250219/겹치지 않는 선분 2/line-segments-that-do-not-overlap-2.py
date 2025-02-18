n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
sorted_lines = sorted(lines, key=lambda x: x[0])

# Logic : as long as the next line doesn't end before the previous line,
# Lines do not overlap

# Naive approach can be solved with Brute force O(n^2), but my approach would
# sort and run through the input once. O(nlogn)

# Return the number of non-overlapping lines


appropriate_lines = n
for i in range(n - 1):
    curr_begin_x, curr_end_x = sorted_lines[i]
    next_begin_x, next_end_x = sorted_lines[i + 1]

    if next_end_x < curr_end_x:
        appropriate_lines -= 2
        i += 2

if appropriate_lines < 0:
    appropriate_lines = 0
print(appropriate_lines)
n, m, k = map(int, input().split())
k -= 1
grid = [list(map(int, input().split())) for _ in range(n)]

# Check if the block fits in the selected row.
def is_valid(row):
    for col in range(k, k + m):
        if col >= n or grid[row][col] == 1:
            return False
    return True

# Fills empty space in a grid with a block.
def fill(row):
    for col in range(k, k + m):
        grid[row][col] = 1

# Main algorithm.
rowIdx = -1
for i in range(n):
    if is_valid(i):
        rowIdx = i
    else:
        break

if rowIdx >= 0:
    fill(rowIdx)

for row in grid:
    print(" ".join(map(str, row)))
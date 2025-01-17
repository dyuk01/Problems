x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Create empty 2d matrix.
# - Find max for x and y

max_x, max_y = 0, 0
for x in x2:
    if x > max_x:
        max_x = x

for y in y2:
    if y > max_y:
        max_y = y

grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

# Take input and mark occupied as "1".
# Last input will set to "0".
rec_count = 1
for x, y, dx, dy, in zip(x1, y1, x2, y2):
    if (rec_count != 3):
        for y_pos in range(y, dy):
            for x_pos in range(x, dx):
                grid[y_pos][x_pos] = 1
    else:
        for y_pos in range(y, dy):
            for x_pos in range(x, dx):
                grid[y_pos][x_pos] = 0        
    rec_count += 1

# Add all "1"s.
res = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 1:
            res += 1

print(res)
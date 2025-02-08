n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
grid = [[0 for _ in range(n)] for _ in range(n)]
nav = [[1,0],[-1,0],[0,1],[0,-1]]

# Function that checks grid's coordinate's bound
def isInBound(y, x):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

# Color the cells
for i in range(m):
    y, x = points[i]
    y -= 1
    x -= 1
    grid[y][x] = 1

    cell_counter = 0
    for j in range(len(nav)):
        # If the 3 or more neighbors are colored,
        # increment the counter
        dy, dx = nav[j]
        new_y = y + dy
        new_x = x + dx
        if isInBound(new_y, new_x) and grid[new_y][new_x] == 1:
            cell_counter += 1

    if cell_counter == 3:
        print(1)
    else:
        print(0)
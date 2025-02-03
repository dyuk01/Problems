n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# E, W, N, S direction
nav = [[0,1],[0,-1],[1,0],[-1,0]]

# Function that checks coordinate's bound
def is_bound(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

# Main algorithm.
res = 0
for i in range(n):
    for j in range(n):
        count = 0
        for dy, dx in nav:
            new_y = i + dy
            new_x = j + dx
            if is_bound(new_y, new_x) and grid[new_y][new_x] == 1:
                count += 1
        if count >= 3:
            res += 1

print(res)
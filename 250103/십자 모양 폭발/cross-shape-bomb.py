n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Function for handling explosion.
def explode(grid: list, r: int, c: int) -> list:
    explosion_size = grid[r][c]
    temp = [[0 for _ in range(n)] for _ in range(n)]
    
    # If explosion_size is larger than grid size, change the explosion_size to n.
    if explosion_size > n:
        explosion_size = n

    # Explosion occurred. Making every cell affected by the explosion to 0.
    for i in range(explosion_size):
        explosion_radius = i
        if r - explosion_radius >= 0:
            grid[r - explosion_radius][c] = 0
        if r + explosion_radius < n:
            grid[r + explosion_radius][c] = 0
        if c - explosion_radius >= 0:
            grid[r][c - explosion_radius] = 0
        if c + explosion_radius < n:
            grid[r][c + explosion_radius] = 0
    
    # Copy every non-zero cells to temp, only by columns--bottom to up--since they are affected by gravity.
    for col in range(n):
        tempRowIdx = 0
        for row in range(n - 1, -1, -1):
            currElement = grid[row][col]
            if currElement != 0:
                temp[tempRowIdx][col] = currElement
                tempRowIdx += 1
        
    
    return temp

# Main algorithm to print a grid.
res = explode(grid, r - 1, c - 1)

# Since the algorithm is iterated from bottom to up, reverse the order
res.reverse()

for row in res:
    print(" ".join(map(str, row)))
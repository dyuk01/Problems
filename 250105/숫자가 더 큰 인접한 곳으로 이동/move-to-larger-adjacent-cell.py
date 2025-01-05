n, r, c = map(int, input().split())
r -= 1
c -= 1
grid = []

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# List of direction in order. (Up, Down, Left, Right)
dir = [[-1,0], [1,0], [0,-1], [0,1]]

# Recursive function that changes the position until it cannot progress any further.
def move(res, y, x):
    currElement = grid[y][x]
    res.append(currElement)

    for dy, dx in dir:
        newY = y + dy
        newX = x + dx
        if newY >= 0 and newY < n and newX >= 0 and newX < n:
            newElement = grid[newY][newX]
            if newElement > currElement:
                move(res, newY, newX)
                break
    
    return


res = []
move(res, r, c)
print(" ".join(map(str, res)))
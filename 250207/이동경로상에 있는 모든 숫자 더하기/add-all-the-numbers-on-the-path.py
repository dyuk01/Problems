N, T = map(int, input().split())
orders = input()
board = [list(map(int, input().split())) for _ in range(N)]

# n * n matrix, start at the middle moving to North
# T num of orders, Left, Right, Force

# Function that rotates the direction
# Output : adjusted [y, x]

# L : -1,0 / 0,-1 / 1,0 / 0,1
# R : -1,0 / 0,1 / 1,0 / 0,-1
def rotate(direction, dy, dx):
    # Rotate Left.
    if direction == "L":
        if dy != 0:
            dx = dy
            dy = 0
        elif dx != 0:
            dy = -1 * dx
            dx = 0

    # Rotate Right.
    else:
        if dy != 0:
            dx = -1 * dy
            dy = 0
        elif dx != 0:
            dy = dx
            dx = 0
    
    return dy, dx

# Function that checks inbound
# Output : bool
def isInBound(y, x):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    return True

# Find the middle point
y, x = N // 2, N // 2

# Set original direction, which is North
dy = -1
dx = 0
numSum = board[y][x]

for i in range(T):
    order = orders[i]
    # Rotate direction
    if order == "L" or order == "R":
        dy, dx = rotate(order, dy, dx)
        continue
    # Move
    elif isInBound(y + dy, x + dx):
        y += dy
        x += dx
        numSum += board[y][x]

print(numSum)
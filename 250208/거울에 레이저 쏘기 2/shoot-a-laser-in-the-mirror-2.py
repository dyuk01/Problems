n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Each cell is a mirror consisted of \ or /
# Amount of lasers = 4 * N
# Result : amount of laser reflections

# n : amount of mirrors per side
# Descriptions of mirror
# k = Mirror index of starting laser
# Index starts from top left and rotates clockwise

# Function checks coordinate's bound
# Output : Bool
def is_outOfBound(i, j):
    return i < 0 or j < 0 or i >= n or j >= n

# Function that sets laser's initial direction
# Output : (i, j)
def setDirection(d):
    if d == "N":
        return 1, 0
    elif d == "E":
        return 0, -1
    elif d == "S":
        return -1, 0
    elif d == "W":
        return 0, 1

# Function that calculates the mirror's initial index
# Output : mirror coordinate(i,j), direction
def findMirrorIdx(k):
    # 0-index
    k -= 1
    # Case1: Laser comes from top
    if k < n:
        return 0, k, "N"
    # Case2: Laser comes from right
    elif k < 2 * n:
        return k - n, k % n, "E"
    # Case3: Laser comes from bottom
    elif k < 3 * n:
        return n - 1, 3 * n - (k + 1), "S"
    # Case4: Laser comes from left
    elif k < 4 * n:
        return 4 * n - (k + 1), 0, "W"

# Main Algorithm.
# Find the starting mirror index and laser's direction.
i, j, direction = findMirrorIdx(k)
di, dj = setDirection(direction)
res = 0

while not is_outOfBound(i, j):
    if di == 0 and dj == 1:
        # Case1: Laser moves right
        # \ : Moves down
        # / : Moves up
        if grid[i][j] == '\\':
            di = 1
            dj = 0
        elif grid[i][j] == '\/':
            di = -1
            dj = 0
    elif di == 0 and dj == -1:    
        # Case2: Laser moves left
        # \ : Moves up
        # / : Moves down
        if grid[i][j] == '\\':
            di = -1
            dj = 0
        elif grid[i][j] == '\/':
            di = 1
            dj = 0
    elif di == -1 and dj == 0:
        # Case3: Laser moves up
        # \ : Moves left
        # / : Moves right
        if grid[i][j] == '\\':
            di = 0
            dj = -1
        elif grid[i][j] == '\/':
            di = 0
            dj = 1
    elif di == 1 and dj == 0:
        # Case4: Laser moves down
        # \ : Moves right
        # / : Moves left
        if grid[i][j] == '\\':
            di = 0
            dj = 1
        elif grid[i][j] == '\/':
            di = 0
            dj = -1
    res += 1
    i += di
    j += dj

print(res)
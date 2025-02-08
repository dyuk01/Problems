n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Each cell is a mirror consisted of \ or /
# Potential starting point = 4 * N
# Result : amount of laser reflections

# n : size

# Descriptions of mirror:
#   k = Starting position
#   Index starts from top left and rotates clockwise

# is_inbound checks coordinate's bound
def is_inbound(i, j):
    return i >= 0 and j >= 0 and i < n and j < n

# init_coord calculates initial position and laser's direction
def init_coord(k):
    # 0-index
    k -= 1
    q = k // n
    r = k % n

    # Case1: Laser comes from top
    if q == 0:
        return 0, r, 1, 0
    # Case2: Laser comes from right
    elif q == 1:
        return r, n - 1, 0, -1
    # Case3: Laser comes from bottom
    elif q == 2:
        return n - 1, n - 1 - r, -1, 0
    # Case4: Laser comes from left
    elif q == 3:
        return n - 1 - r, 0, 0, 1

# reflect changes the laser's direction based on mirror's type
def reflect(mirror, di, dj):
    if mirror == '\\':
        if di == 0 and dj == 1:
            di = 1
            dj = 0
        elif di == 0 and dj == -1:
            di = -1
            dj = 0
        elif di == 1 and dj == 0:
            di = 0
            dj = 1
        elif di == -1 and dj == 0:
            di = 0
            dj = -1

    elif mirror == '/':
        if di == 0 and dj == 1:
            di = -1
            dj = 0
        elif di == 0 and dj == -1:
            di = 1
            dj = 0
        elif di == 1 and dj == 0:
            di = 0
            dj = -1
        elif di == -1 and dj == 0:
            di = 0
            dj = 1
    
    return di, dj

# Main Algorithm.
# Find the starting mirror index and laser's direction.
i, j, di, dj = init_coord(k)
res = 0

while is_inbound(i, j):
    res += 1
    di, dj = reflect(grid[i][j], di, dj)
    i += di
    j += dj

print(res)
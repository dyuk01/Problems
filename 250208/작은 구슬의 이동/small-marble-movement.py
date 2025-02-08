n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Write your code here!

# 1-indexed grid
# If out of bound, change to opposing direction without moving == 1 second
# n = grid size
# t = seconds after
# r, c == original position of the marvel
# d = direction --> Up, Down, Right, Left

# Initialize direction in order
nav = [[-1,0], [1,0], [0,1], [0,-1]]

# function that checks if marvel goes out of bound
def isInBound(y, x):
    if x < 1 or y < 1 or x > n or y > n:
        return False
    return True

# Function that changes direction
def change_direction(direction):
    if direction == "U":
        direction = "D"
    elif direction == "D":
        direction = "U"
    elif direction == "R":
        direction = "L"
    else:
        direction = "R"
    
    return direction


y, x = r, c
# Start from the original grid, and follow the instruction
for i in range(t):
    if d == "U":
        dy, dx = nav[0]
    elif d == "D":
        dy, dx = nav[1]        
    elif d == "R":
        dy, dx = nav[2]
    else:
        dy, dx = nav[3]
    
    if not isInBound(y + dy, x + dx):
        d = change_direction(d)
        continue
    
    x += dx
    y += dy

print(y, x)
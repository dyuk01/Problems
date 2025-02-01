n, m = map(int, input().split())

a = []
for _ in range(n):
    direction, time = input().split()
    a.append((direction, int(time)))

b = []
for _ in range(m):
    direction, time = input().split()
    b.append((direction, int(time)))

def define_direction(direction):
    if direction == "L":
        return -1
    return 1

# 1. Initialize array according to their max time
def init_array(arr):
    movement = []
    pos = 0
    for direction, time in arr:
       for _ in range(time):
        pos += define_direction(direction)
        movement.append(pos) 

    return movement    

a_movement = init_array(a)
b_movement = init_array(b)

# 3. Record each position in the array, then return
# when the pos for A and B match
def solution():
    for i in range(len(a_movement)):  
        if a_movement[i] == b_movement[i]:
            return i + 1
    return -1
        
print(solution())
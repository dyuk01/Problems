n, m = map(int, input().split())

a = []
for _ in range(n):
    direction, time = input().split()
    a.append((direction, int(time)))

b = []
for _ in range(m):
    direction, time = input().split()
    b.append((direction, int(time)))

# Write your code here!

# 1. Find the max time for a and b
max_time = 1
for direction, time in a:
    max_time += time

# 2. Initialize array according to their max time
a_movement = [0] * max_time
curr_a = 0
a_idx = 1
for direction, time in a:
    for _ in range(time):
        if direction == "L":
            curr_a -= 1
        else:
            curr_a += 1
        a_movement[a_idx] = curr_a 
        a_idx += 1

b_movement = [0] * max_time
curr_b = 0
b_idx = 1
for direction, time in b:
    for _ in range(time):
        if direction == "L":
            curr_b -= 1
        else:
            curr_b += 1
        b_movement[b_idx] = curr_b 
        b_idx += 1

# 3. Record each position in the array, then return
# when the pos for A and B match
res = float('inf')
for i in range(1, max_time):
    if a_movement[i] == b_movement[i]:
        res = i
        print(i)
        break

if res == float('inf'):
    print(-1)

n = int(input())
seats = input()

# Please write your code here.
# Iterate through the array to find the distance from left to right
dist_l = [[0] for _ in range(n)]
for i in range(n):
    if seats[i] == '1':
        counter = 0
    elif seats[i] == '0':
        counter += 1
    
    dist_l[i] = counter

counter = 0
# Iterate through the array to find the distance from right to left
dist_r = [[0] for _ in range(n)]
for i in range(n - 1, -1, -1):
    if seats[i] == '1':
        counter = 0
    elif seats[i] == '0':
        counter += 1
    
    dist_r[i] = counter

# Find the first and last occruences of occupied seat
occupied = []
l, r = -1, -1
for i in range(n):
    if seats[i] == '1':
        occupied.append(i)

if len(occupied) == 1:
    l = occupied[0]
elif len(occupied) > 1:
    l = min(occupied)
    r = max(occupied)

# Take the minimum of the 2 arrays, to find the minimum distances
dist_min = [[0] for _ in range(n)]
for i in range(n):
    if i < l:
        dist_min = dist_r[i]
    elif l <= i and i <= r:
        dist_min[i] = min(dist_l[i], dist_r[i])
    elif r < i:
        dist_min[i] = dist_l[i]

# Take the maximum distance of the minimum distances to find the answer
print(max(dist_min))
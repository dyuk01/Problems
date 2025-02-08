n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

minSum = float('inf')
for i in range(1, n - 1):
    dist = 0
    prev = 0
    for j in range(1, n):
        if i == j:
            continue
        dist += abs(points[j][0] - points[prev][0])
        dist += abs(points[j][1] - points[prev][1])
        prev = j
    
    if dist < minSum:
        minSum = dist

print(minSum)

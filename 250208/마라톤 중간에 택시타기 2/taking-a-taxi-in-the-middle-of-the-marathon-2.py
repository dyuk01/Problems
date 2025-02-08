n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

minSum = float('inf')
for i in range(1, n - 1):
    dist = 0
    prev_x = x[0]
    prev_y = y[0]
    for j in range(1, n):
        if i == j:
            continue
        dist += abs(x[j] - prev_x)
        dist += abs(y[j] - prev_y)
        prev_x = x[j]
        prev_y = y[j]
    
    if dist < minSum:
        minSum = dist

print(minSum)

n = int(input())

y = []
x = []
for _ in range(n):
    i, j = list(map(int, input().split()))
    y.append(i)
    x.append(j)


min_area = float('inf')
for i in range(n):
    min_y, min_x = float('inf'), float('inf')
    max_y, max_x = 0, 0
    for j in range(n):
        if i == j:
            continue
        min_y, min_x = min(min_y, y[j]), min(min_x, x[j])
        max_y, max_x = max(max_y, y[j]), max(max_x, x[j])
        
    area = (max_y - min_y) * (max_x - min_x)
    min_area = min(min_area, area)

print(min_area)
        
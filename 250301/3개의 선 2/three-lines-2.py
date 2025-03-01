n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def sol():
    x_coords = sorted(list(set(p[0] for p in points)))
    y_coords = sorted(list(set(p[1] for p in points)))

    if len(x_coords) <= 3 or len(y_coords) <= 3:
        return 1
    
    for i in range(len(y_coords)):
        for j in range(i + 1, len(x_coords)):
            crossed = set()
            for p in points:
                if p[1] == y_coords[i] or p[1] == y_coords[j]:
                    crossed.add(p)
        

            remain = set(points) - crossed
            if not remain:
                return 1
            
            remain_x = set(p[0] for p in remain)
            if len(remain_x) == 1:
                return 1
    
    for i in range(len(x_coords)):
        for j in range(i + 1, len(x_coords)):
            crossed = set()
            for p in points:
                if p[0] == x_coords[i] or p[0] == x_coords[j]:
                    crossed.add(p)
            
            remain = set(points) - crossed
            if not remain:
                return 1
            remain_y = set(p[1] for p in remain)
            if len(remain_y) == 1:
                return 1
    
    return 0

print(sol())
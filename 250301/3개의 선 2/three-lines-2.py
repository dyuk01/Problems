from typing import Tuple, List

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def check_2_1(coords: List[Tuple[int, int]], axis: int):
    """
    axis = 0: x-axis
    axis = 1: y-axis
    """
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            not_crossed = set()
            for p in points:
                if not (p[axis] == coords[i] or p[axis] == coords[j]):
                    not_crossed.add(p)

            remain = {p[axis ^ 1] for p in not_crossed}
            if len(remain) == 1:
                return 1
    return 0

def sol():
    x_coords = sorted({p[0] for p in points})
    y_coords = sorted({p[1] for p in points})

    # Case1: All x-lines or y-lines
    if len(x_coords) <= 3 or len(y_coords) <= 3:
        return 1
    
    # Case2: Check 2_1 lines
    return check_2_1(x_coords, 0) | check_2_1(y_coords, 1)

print(sol())


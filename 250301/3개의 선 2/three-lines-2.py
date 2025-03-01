# n = int(input())
# points = [tuple(map(int, input().split())) for _ in range(n)]

# def sol():
#     x_coords = sorted(list(set(p[0] for p in points)))
#     y_coords = sorted(list(set(p[1] for p in points)))

#     # Case1: All x-lines or y-lines
#     if len(x_coords) <= 3 or len(y_coords) <= 3:
#         return 1
    
#     # Case2: 2 y-lines and 1 x-line
#     for i in range(len(y_coords)):
#         for j in range(i + 1, len(x_coords)):
#             crossed = set()
#             for p in points:
#                 if p[1] == y_coords[i] or p[1] == y_coords[j]:
#                     crossed.add(p)
        
#             remain = set(points) - crossed
#             if not remain:
#                 return 1
            
#             remain_x = set(p[0] for p in remain)
#             if len(remain_x) == 1:
#                 return 1
    
#     # Case3: 1 y-line and 2 x-lines
#     for i in range(len(x_coords)):
#         for j in range(i + 1, len(x_coords)):
#             crossed = set()
#             for p in points:
#                 if p[0] == x_coords[i] or p[0] == x_coords[j]:
#                     crossed.add(p)
            
#             remain = set(points) - crossed
#             if not remain:
#                 return 1
#             remain_y = set(p[1] for p in remain)
#             if len(remain_y) == 1:
#                 return 1
    
#     return 0

# print(sol())

from typing import Tuple, List

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


def covers(axis: str, val: int, point: Tuple[int, int]) -> bool:
    if axis == "x":
        return val == point[0]
    if axis == "y":
        return val == point[1]

def solution() -> bool:
    if len(points) <= 3:
        return True

    all_x = sorted({p[0] for p in points})
    all_y = sorted({p[1] for p in points})
    if len(all_x) <= 3 or len(all_y) < 3:
        return True

    candidates = [("x", v) for v in all_x] + [("y", v) for v in all_y]

    num_lines = len(candidates)
    for i in range(num_lines - 2):
        axis1, val1 = candidates[i]        
        for j in range(i + 1, num_lines - 1):
            axis2, val2 = candidates[j]
            for k in range(j + 1, num_lines):
                axis3, val3 = candidates[k]
                leftover = []
                for p in points:
                    if covers(axis1, val1, p) or covers(axis2, val2, p) or covers(axis3, val3, p):
                        continue
                    leftover.append(p)
                
                if not leftover:
                    return True
    return False

print(1 if solution() else 0)

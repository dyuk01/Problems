x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.


def solution()-> str:
    # Case1: 3 < 2
    if x1 <= x3:
        if x3 <= x2:
            return "intersecting"

    # Case2: 1 < 4
    elif x3 <= x1:
        if x1 <= x4:
            return "intersecting"
    
    return "nonintersecting"

print(solution())
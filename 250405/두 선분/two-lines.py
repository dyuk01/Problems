x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.

def sol():
    # Case1: x2 <= a1
    if x1 <= a1:
        if x2 <= a1:
            return "intersecting"

    # Case2: a2 <= x1
    if a1 <= x1:
        if a2 <= x1:
            return "intersecting"

    # Case3: y2 <= b1
    if y1 <= a1:
        if y2 <= b1:
            return "intersecting"

    # Case4: b2 <= y1
    if a1 <= y1:
        if b2 <= y1:
            return "intersecting"
    
    return "nonintersecting"

print(sol())

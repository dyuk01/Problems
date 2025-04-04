x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.


# Case1: 3 < 2
# Case2: 1 < 4

if x3 < x2 or x1 < x4:
    print("intersecting")
else:
    print("nonintersecting")
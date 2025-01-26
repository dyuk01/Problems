x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())


def is_inbound(x, y):
    return x1[0] < x < x2[0] and y1[0] < y < y2[0]

def get_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

if is_inbound(x1[1], y1[1]) or is_inbound(x1[1], y2[1]) or is_inbound(x2[1], y1[1]) or is_inbound(x2[1], y2[1]):
    # Case 1: Any new input is inside 1st rectangle.
    # output: Area(R0)
    print(get_area(x1[0], y1[0], x2[0], y2[0]))
else:
    if (x1[1] <= x1[0] and y1[1] <= y1[0]) and (x2[0] <= x2[1] and y2[0] <= y2[1]):
        # Case 2-1: New rectangle greater than original.
        # output: 0
        print(0)
    else:
        # Case 2-2: Split middle.
        # output: Area(R0)
        if (x1[0] < x1[1] and x2[1] < x2[0] and y1[1] <= y1[0] and y2[0] <= y2[1]) or (x1[1] <= x1[0] and x2[0] <= x2[1] and y1[0] < y1[1] and y2[1] < y2[0]):
            print(get_area(x1[0], y1[0], x2[0], y2[0]))
        else:
            # Case 2-3: Cut edge.
            # output: Area(R*)
            # Cut left
            print(get_area(x2[1], y1[0], x2[0], y2[0]))
            # Cut bottom
            print(get_area(x1[0], y2[1], x2[0], y2[0]))
            # Cut right
            print(get_area(x1[0], y1[0], x1[1], y2[0]))
            # Cut top
            print(get_area(x1[0], y1[0], x2[0], y1[1]))



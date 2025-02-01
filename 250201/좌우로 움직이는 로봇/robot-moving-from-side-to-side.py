n, m = map(int, input().split())

# Process robot A's movements
a_movements = []
for _ in range(n):
    t, d = input().split()
    a_movements.append((int(t), d))


# Process robot B's movements
b_movements = []
for _ in range(m):
    t, d = input().split()
    b_movements.append((int(t), d))

def determine_direction(direction):
    if direction == "L":
        return -1
    return 1

def init_movements(arr):
    pos = 0
    movements = []
    movements.append(0)

    for t, d in arr:
        for _ in range(t):
            pos += determine_direction(d)
            movements.append(pos)
    return movements

# Position per second
a = init_movements(a_movements)
b = init_movements(b_movements)

res = 0

min_l = min(len(a), len(b))

for i in range(1, min_l):
    if a[i] == b[i] and a[i - 1] != b[i - 1]:
        res += 1

# TODO: Check edgecase1 - One stays still, while another go back and forth
# A is always shorter than B
if len(a) > len(b):
    temp = a
    a = b
    b = temp

for i in range(len(a), len(b)):
    if a[-1] == b[i] and a[-1] != b[i - 1]:
        res += 1

print(res)
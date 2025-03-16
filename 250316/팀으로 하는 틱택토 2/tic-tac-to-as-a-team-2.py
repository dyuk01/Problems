inp = [input() for _ in range(3)]

# Please write your code here.

res = 0

# Count answer vertically
for i in range(3):
    if len(set(inp[i])) == 2:
        res += 1

# Count answer horizontally
for j in range(3):
    num_v = set()
    for i in range(3):
        num_v.add(inp[i][j])
    if len(set(num_v)) == 2:
        res += 1

# Count answer diagonally
num_d = set()
for i in range(3):
    num_d.add(inp[i][i])

if len(set(num_d)) == 2:
    res += 1

num_d = set()
for i in range(3):
    num_d.add(inp[i][2 - i])

if len(set(num_d)) == 2:
    res += 1

print(res)

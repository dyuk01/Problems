inp = [input() for _ in range(3)]

# Please write your code here.

res = 0
answers = []

# Count answer vertically
for i in range(3):
    if len(set(inp[i])) == 2 and set(inp[i]) not in answers:
        res += 1
        answers.append(set(inp[i]))

# Count answer horizontally
for j in range(3):
    num_v = set()
    for i in range(3):
        num_v.add(inp[i][j])
    if len(set(num_v)) == 2 and num_v not in answers:
        res += 1
        answers.append(num_v)

# Count answer diagonally
num_d = set()
for i in range(3):
    num_d.add(inp[i][i])

if len(set(num_d)) == 2 and num_d not in answers:
    res += 1
    answers.append(num_d)

num_d = set()
for i in range(3):
    num_d.add(inp[i][2 - i])

if len(set(num_d)) == 2 and num_d not in answers:
    res += 1
    answers.append(num_d)

print(res)

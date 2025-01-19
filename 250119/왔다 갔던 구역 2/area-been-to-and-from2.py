n = int(input())
movement = []
for _ in range(n):
    xi, di = input().split()
    movement.append((int(xi), di))

# counter = {}
# for i in range(-1000, 1000):
#     counter[i] = 0

# curr = 0
# for pos, d in movement:
#     if d == "L":
#         pos *= -1

#     if curr + pos > curr:
#         for i in range(curr, curr + pos):
#             counter[i] += 1
#     else:
#         for i in range(curr + pos, curr):
#             counter[i] += 1
    
#     curr = curr + pos

# res = 0
# for count in counter.values():
#     if count >= 2:
#         res += 1 

# print(res)

# Set up
d = {}
for i in range(-1000, 1000):
    d[i] = False
d[0] = True

# iter moves
idx = 0
s = set()
for xi, di in movement:
    if di == "R":
        for j in range(idx, idx + xi):
            if not d[j]:
                d[j] = True
            elif j not in s:
                s.add(j)
        idx = idx + xi

    elif di == "L":
        for j in range(idx - 1, idx - xi - 1, -1):
            if not d[j]:
                d[j] = True
            elif j not in s:
                s.add(j)
        idx = idx - xi

print(len(s))
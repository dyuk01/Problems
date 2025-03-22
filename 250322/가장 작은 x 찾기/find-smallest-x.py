import math

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.
# a_i <= n * 2^(i+1) <= b_i

# res = []
# for i in range(n):
#     ceil = math.ceil(a[i] / pow(2, i+1))
#     floor = math.floor(b[i] / pow(2, i+1))
#     print(ceil, floor)
#     for j in range(ceil, floor + 1):
#         if j not in res:
#             res.append(j)
#         else:
#             res.remove(j)

# print(res)

res = []
ceil = math.ceil(a[n - 1] / pow(2, n))
floor = math.floor(b[n - 1] / pow(2, n))

for i in range(ceil, floor + 1):
    res.append(i)

print(min(res))
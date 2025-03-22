import math

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.
# a_i <= n * 2^(i+1) <= b_i

intervals = []
for i in range(n):
    factor = pow(2, i+1)
    ceil = math.ceil(a[i] / factor)
    intervals.append(ceil)

print(max(intervals))

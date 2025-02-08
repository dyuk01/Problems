n = int(input())
A = list(map(int, input().split()))

# Write your code here!
# 1-index
# Focus : House
# output : min sum of all dist

minSum = float('inf')
for i in range(n):
    dist = 0
    for j in range(n):
        dist += A[j] * (abs(i - j))
    if dist < minSum:
        minSum = dist

print(minSum)
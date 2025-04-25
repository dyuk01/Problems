n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()

m = 2 * n
l = arr[:m//2]
r = arr[m//2:]

min_diff = float('inf')

for i in range(n):
    min_diff = min(min_diff, r[i] - l[i])

print(min_diff)
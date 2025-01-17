a, b, c = map(int, input().split())

# Write your code here!
res = 0

if a > 11:
    res += (a - 11) * 24 * 60
if b > 11:
    res += (b - 11) * 60
if c > 11:
    res += (c - 11)

print(res)
a, b, c = map(int, input().split())

# Write your code here!
res, day, hr, m = 0, 0, 0, 0

day = (a - 11) * 60 * 24
hr = (b - 11) * 60
m = c - 11

res = day + hr + m

print(res)
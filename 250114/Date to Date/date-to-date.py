m1, d1, m2, d2 = map(int, input().split())
m1 -= 1
m2 -= 1

# Month days from Jan to Dec
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_day = 0
for i in range(m1, m2 + 1):
    total_day += days[i]

day_diff = d1 + (days[m2] - d2) - 1

print(total_day - day_diff)
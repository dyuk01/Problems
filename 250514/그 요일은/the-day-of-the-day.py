m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
odd_months = [1,3,5,7,8,10,12]
even_months = [4,6,9,11]
extra_month = [2]

# Find the total days within the time period.
total_days, month_days = 0, 0
for m in range(m1, m2 + 1):
    if m in odd_months:
        month_days += 31
    elif m in even_months:
        month_days += 30
    else:
        month_days += 29
    
    total_days += month_days
    if m == m2:
        last_month_days = month_days

total_days -= d1 - 1
total_days -= last_month_days - d2

# Find repeating week -> Subtract desired day - Monday
days = {
    'Mon' : 0,
    'Tue' : 1,
    'Wed' : 2,
    'Thu' : 3,
    'Fri' : 4,
    'Sat' : 5,
    'Sun' : 6
}

total_days -= days[A]

print(total_days // 7 + 1)

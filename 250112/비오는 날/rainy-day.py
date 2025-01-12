n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Write your code here!
class Forecast:

    date: str
    day: str
    weather: str

    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

    # def __sort__(self,)
    def printer(self):
        print(self.date, self.day, self.weather)

f = []
for i in range(n):
    if weather[i] == "Rain":
        f.append(Forecast(date[i], day[i], weather[i]))

f.sort(key=lambda x: x.date)
f[0].printer()
    
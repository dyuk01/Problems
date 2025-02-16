devs = list(map(int, input().split()))
n = 6

# Need to form 2 teams consisted of 3
# Return the minimum difference between the teams

# Function that finds the minimum ability between the teams
def find_diff(i, j, k):
    team1 = devs[i] + devs[j] + devs[k]
    team2 = sum(devs) - team1
    return abs(team1 - team2)

min_diff = float('inf')
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            min_diff = min(min_diff, find_diff(i, j, k))

print(min_diff)
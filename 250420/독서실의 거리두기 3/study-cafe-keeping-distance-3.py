n = int(input())
seats = input()

# Please write your code here.
positions = []
for i in range(n):
    if num == '1':
        positions.append(i)

min_distance = float('inf')
optPos = -1

for pos in range(n):
    if seats[pos] == '1':
        continue

    
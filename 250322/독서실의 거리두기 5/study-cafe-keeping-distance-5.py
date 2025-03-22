n = int(input())
seats = input()

# Please write your code here.
occupied = []

for i in range(n):
    if seats[i] == '1':
        occupied.append(i)

max_min_dist = 0

for i in range(n):
    if seats[i] == '0':
        temp_occupied = occupied + [i]
        temp_occupied.sort()

        min_dist = float('inf')
        for j in range(1, len(temp_occupied)):
            dist = temp_occupied[j] - temp_occupied[j - 1]
            min_dist = min(min_dist, dist)
        
        max_min_dist = max(max_min_dist, min_dist)

print(max_min_dist)

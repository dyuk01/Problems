n = int(input())
circles = [int(input()) for _ in range(n)]

# Each cell --> 2 doors and moves counter clockwise
# All people start at same room
minSum = float('inf')
for i in range(n):
    # Iterate through and find start point

    tempSum = 0
    for j in range(i + 1, i + n):
        # Iterate through the remaining rooms
        distance = j - i
        tempSum += circles[j % n] * distance

    if tempSum < minSum:
        minSum = tempSum
    
print(minSum)
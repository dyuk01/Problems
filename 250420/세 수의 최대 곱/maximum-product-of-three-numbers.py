n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

max1, max2, max3 = -float('inf'), -float('inf'), -float('inf')
min1, min2 = float('inf'), float('inf')

for num in arr:
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num
    
    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num

print(max(max1 * max2 * max3, max1 * min1 * min2))
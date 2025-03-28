n = int(input())
heights = [int(input()) for _ in range(n)]

# Please write your code here.
def carve_hills()-> int:
    min_cost = float('inf')
    low, high = min(heights), max(heights)
    height_diff = (high - low) - 17

    if (height_diff < 0):
        return -1

    for dl in range(1, height_diff):
        dh = height_diff - dl
        
        cost = 0
        for h in heights:
            if h < low + dl:
                cost += ((low + dl) - h) ** 2
            
            if h > high - dh:
                cost += (h - (high - dh)) ** 2
        
        min_cost = min(min_cost, cost)
    
    return min_cost

print(carve_hills())

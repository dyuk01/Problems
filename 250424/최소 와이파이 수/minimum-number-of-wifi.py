n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
arr.append(0)

def solution()-> int:
    # Base case
    if m == 0:
        return sum(arr)
    
    # Keep track of how many people there are
    area_populated = []
    count = 0
    for a in arr:
        if a == 1:
            count += 1
        
        if a == 0 and count != 0:
            area_populated.append(count)
            count = 0
    
    wifi = 0
    wifi_power = 2 * m + 1
    for people in area_populated:
        if people % wifi_power == 0:
            wifi += people // wifi_power
        else:
            wifi += people // wifi_power + 1
    
    return wifi

print(solution())

    


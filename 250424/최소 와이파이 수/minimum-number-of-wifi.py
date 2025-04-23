n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

def solution()-> int:
    total_population = sum(arr)
    wifi_power = 2 * m + 1
    wifi = total_population // wifi_power if total_population % wifi_power == 0 else total_population // wifi_power + 1
    
    return wifi

print(solution())

    


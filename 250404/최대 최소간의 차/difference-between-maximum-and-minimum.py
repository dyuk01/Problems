n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_num = min(arr)
max_num = max(arr)
diff = max_num - min_num
min_cost = 0

while diff > k:
    # Calculate the cost of raising minimum
    low_cost = 0
    for num in arr:
        if num < min_num + 1:
            low_cost += 1

    # Calculate the cost of raising maximum 
    high_cost = 0
    for num in arr:
        if num > max_num - 1:
            high_cost += 1
    
    # Adjust the min/max and the cost
    if low_cost <= high_cost:
        min_num += 1
        min_cost += low_cost
    else:
        max_num -= 1
        min_cost += high_cost
    
    diff = max_num - min_num

print(min_cost)
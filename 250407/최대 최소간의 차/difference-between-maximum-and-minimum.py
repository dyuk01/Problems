n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_num = min(arr)
max_num = max(arr)
diff = max_num - min_num
est_cost = 0

while diff > k:
    # Calculate the cost of raising minimum
    # low_cost = 0
    # for num in arr:
    #     if num < min_num + 1:
    #         low_cost += 1
    low_raise_est_cost = sum([1 if num < min_num + 1 else 0 for num in arr])


    # Calculate the cost of reducing maximum 
    # high_cost = 0
    # for num in arr:
    #     if num > max_num - 1:
    #         high_cost += 1
    high_reduce_est_cost = sum([1 if num > max_num - 1 else 0 for num in arr])
    
    
    # Adjust the min/max and the cost
    if low_raise_est_cost <= high_reduce_est_cost:
        min_num += 1
        est_cost += low_raise_est_cost
    else:
        max_num -= 1
        est_cost += high_reduce_est_cost
    
    diff = max_num - min_num

print(est_cost)
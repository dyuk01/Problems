n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

max_sum = 0
for i in range(len(numbers) - 2):
    curr_sum = numbers[i] + numbers[i + 1] + numbers[i + 2] 
    if max_sum < curr_sum:
        max_sum = curr_sum
    
print(max_sum)
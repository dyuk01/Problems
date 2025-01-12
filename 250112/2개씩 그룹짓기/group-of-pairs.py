n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
nums.sort()
sum = []
i, j = 0, 2 * n - 1

while i < j:
    sum.append(nums[i] + nums[j])
    i += 1
    j -= 1

print(max(sum))
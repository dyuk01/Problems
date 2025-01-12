n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

# Function for finding median
def find_med(idx):
    nums = arr[:idx + 1]
    nums.sort()
    return nums[idx // 2]

# Main algorithm.
res = []
for i in range(n):
    if i % 2 == 0:
        res.append(str(find_med(i)))

print(" ".join(res))
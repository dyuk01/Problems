n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
# N -> M - 1 sections to divide into M sections

# dp = [0] * (n + 1)
# for i in range(n):
#     dp[i + 1] = dp[i] + a[i]

# Pre-aggregate the sum values.
presum = [0] * (n + 1)
for i in range(n):
    presum[i + 1] = presum[i] + a[i]

# Compute sum(a[i:j]).
# Reduced time complexity: O(n) -> O(1).
def get_division_sum(i: int, j: int) -> int:
    return presum[j + 1] - presum[i]

# Memoize division results.
div_memo = {}

# Compute minimized max sum of division that start in index i with m division.
def set_division(i: int, m: int) -> int:
    if (i, m) in div_memo:
        return div_memo[(i, m)]

    if m == 1:
        return get_division_sum(i, n - 1)
    
    val = float('inf')
    for j in range(i, n - m + 1):
        left = get_division_sum(i, j)
        right = set_division(j + 1, m - 1)
        val = min(val, max(left, right))
    
    div_memo[(i, m)] = val
    return val


print(set_division(0, m))

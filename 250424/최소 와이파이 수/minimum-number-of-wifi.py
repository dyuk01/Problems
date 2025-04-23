n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
def solution()-> int:
    # Base case
    if m == 0:
        return n

    area_affected = 2 * m + 1

    wifi_needed = n // area_affected if n % area_affected == 0 else n // area_affected + 1
    return wifi_needed

print(solution())

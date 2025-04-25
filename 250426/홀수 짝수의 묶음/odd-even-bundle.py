n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
def solution()-> int:
    odd, even = 0, 0
    # Count even and odds
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if even > odd:
        return odd * 2 + 1 
    if even == odd:
        return even + odd 
    
    res = even * 2
    diff = odd - even
    if diff % 3 == 0:
        res += (diff // 3) * 2
    elif ((diff % 3) % 2 == 0):
        res += diff // 3 * 2 + 1
    else:
        res += diff // 3 * 2 - 1
    
    return res


print(solution())
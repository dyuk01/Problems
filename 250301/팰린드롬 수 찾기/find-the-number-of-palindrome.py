X, Y = map(int, input().split())

# Please write your code here.


def is_palindrome(n):
    str_num = str(n)
    l, r = 0, len(str_num) - 1

    while l <= r:
        if str_num[l] != str_num[r]:
            return False
        l += 1
        r -= 1

    return True

res = 0
for num in range(X, Y + 1):
    if is_palindrome(num):
        res += 1

print(res)
from collections import deque
import math

n = int(input())

# Please write your code here.

# def init_dq() -> deque:
#     return deque([x for x in range(1, n+1)])


# def solution(dq: deque) -> int:
#     while len(dq) > 1:
#         dq.popleft()
#         dq.rotate(-1)

#     return dq.pop()

# print(solution(init_dq()))

def solution() -> int:
    if n < 3:
        return n
    return 2 * (n - 2 ** (n.bit_length() - 1))

print(solution())
# f(n) = 2(n - 2^(n.bit_length)
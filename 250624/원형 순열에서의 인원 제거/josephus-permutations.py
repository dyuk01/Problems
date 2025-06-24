# from collections import deque
# from typing import List

# n, k = map(int, input().split())


# # Please write your code here.
# # Removes k - 1'th push element

# dq = deque([x for x in range(1, n+1)])

# def solution() -> List[int]:
#     res = []
#     while len(dq) > 0:
#         dq.rotate(1 - k)
#         res.append(dq.popleft())

#     return res

# print(' '.join(map(str, solution())))

from collections import deque
from typing import List

n, k = map(int, input().split())

def set_deque() -> deque:
    dq = deque()
    for i in range(1, n+1):
        dq.append(i)
    return dq

def pop_k_repeat(dq: deque) -> List[int]:
    result = []
    while len(dq) > 1:
        dq.rotate(-k+1)
        result.append(dq.popleft())
    return result + [dq[0]]

def solution() -> str:
    return ' '.join(map(str, pop_k_repeat(set_deque())))

print(solution())
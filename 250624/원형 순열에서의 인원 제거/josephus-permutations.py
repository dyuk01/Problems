from collections import deque
from typing import List

n, k = map(int, input().split())

# Please write your code here.
# Removes k - 1'th push element

def solution() -> List[int]:
    dq = deque()
    for i in range(1, n+1):
        dq.append(i)

    res = []
    while len(dq) > 1:
        for _ in range(k-1):
            dq.append(dq.popleft())
        res.append(dq.popleft())
    res.append(dq.popleft())
    
    return res

print(' '.join(map(str, solution())))

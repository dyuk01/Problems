from collections import deque
from typing import List

n, k = map(int, input().split())


# Please write your code here.
# Removes k - 1'th push element

dq = deque([x for x in range(1, n+1)])

def solution() -> List[int]:
    res = []
    while len(dq) > 0:
        # for _ in range(k-1):
        #     dq.append(dq.popleft())
        # res.append(dq.popleft())
        dq.rotate(1 - k)
        res.append(dq.popleft())
    # res.append(dq.popleft())
    
    return res

print(' '.join(map(str, solution())))

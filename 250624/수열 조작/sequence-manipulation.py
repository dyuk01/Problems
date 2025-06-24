from collections import deque

n = int(input())

# Please write your code here.

def solution(n: int) -> int:
    dq = deque()
    for i in range(1, n+1):
        dq.append(i)
    
    while len(dq) > 1:
        dq.popleft()
        if len(dq) == 1:
            break
        dq.append(dq.popleft())
    
    return dq.pop()

print(solution(n))

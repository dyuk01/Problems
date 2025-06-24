from collections import deque

n = int(input())

# Please write your code here.

def solution() -> int:
    dq = deque([x for x in range(1, n+1)])
    while len(dq) > 1:
        dq.popleft()
        dq.rotate(-1)
    return dq.pop()

print(solution())

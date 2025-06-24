from typing import List
from collections import deque

n = int(input())
cmds = []
nums = []

for _ in range(n):
    line = input().split()
    cmds.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        nums.append(int(line[1]))
    else:
        nums.append(0)

# Please write your code here.
class Deque:

    dq: deque

    def __init__(self):
        self.dq = deque()
    

    def push_front(self, a: int) -> None:
        self.dq.appendleft(a)
    

    def push_back(self, a: int) -> None:
        self.dq.append(a)
    

    def pop_front(self) -> int:
        return self.dq.popleft()
    

    def pop_back(self) -> int:
        return self.dq.pop()
    

    def size(self) -> int:
        return len(self.dq)
    

    def empty(self) -> int:
        return int(not self.dq)
    

    def front(self) -> int:
        return self.dq[0]
    

    def back(self) -> int:
        return self.dq[-1]


def solution() -> None:
    dq = Deque()

    for i in range(n):
        cmd, num = cmds[i], nums[i]
        if cmd == "push_front":
            dq.push_front(num)
        elif cmd == "push_back":
            dq.push_back(num)
        elif cmd == "pop_front":
            print(dq.pop_front())
        elif cmd == "pop_back":
            print(dq.pop_back())
        elif cmd == "size":
            print(dq.size())
        elif cmd == "empty":
            print(dq.empty())
        elif cmd == "front":
            print(dq.front())
        elif cmd == "back":
            print(dq.back())

solution()
    
# from typing import List
# from collections import deque

# n = int(input())
# cmd = []
# num = []

# for _ in range(n):
#     line = input().split()
#     cmd.append(line[0])
#     if line[0] in ["push_front", "push_back"]:
#         num.append(int(line[1]))
#     else:
#         num.append(0)

# # Please write your code here.
# class Deque:

#     dq: deque()

#     def __init__(self):
#         self.dq = deque()
    

#     def push_front(self, a: int) -> None:
#         self.dq.appendleft(a)
    

#     def push_back(self, a: int) -> None:
#         self.dq.append(a)
    

#     def pop_front(self) -> int:
#         return self.dq.popleft()
    

#     def pop_back(self) -> int:
#         return self.dq.pop()
    

#     def size(self) -> int:
#         return len(self.dq)
    

#     def empty(self) -> int:
#         return int(not self.dq)
    

#     def front(self) -> int:
#         return self.dq[0]
    

#     def back(self) -> int:
#         return self.dq[-1]


# def solution(n: int) -> None:
#     dq = Deque()

#     for i in range(n):
#         c, n = cmd[i], num[i]
#         if c == "push_front":
#             dq.push_front(n)
#         elif c == "push_back":
#             dq.push_back(n)
#         elif c == "pop_front":
#             print(dq.pop_front())
#         elif c == "pop_back":
#             print(dq.pop_back())
#         elif c == "size":
#             print(dq.size())
#         elif c == "empty":
#             print(dq.empty())
#         elif c == "front":
#             print(dq.front())
#         elif c == "back":
#             print(dq.back())

# solution(n)
    

from typing import List

n = int(input())
cmds = []
nums = []

for _ in range(n):
    line = input().split()
    cmds.append(line[0])
    if line[0] in ['push_front', 'push_back']:
        nums.append(int(line[1]))
    else:
        nums.append(0)

class Deque:
    dq: List[int]

    def __init__(self):
        self.dq = []

    def size(self) -> int:
        return len(self.dq)
    
    def empty(self) -> int:
        return int(not self.dq)
    
    def front(self) -> int:
        return self.dq[0] if self.dq else 0
    
    def back(self) -> int:
        return self.dq[-1] if self.dq else 0
    
    def push_front(self, x: int) -> None:
        self.dq.insert(0, x)

    def push_back(self, x: int) -> None:
        self.dq.append(x)

    def pop_front(self) -> int:
        return self.dq.pop(0) if self.dq else 0
    
    def pop_back(self) -> int:
        return self.dq.pop() if self.dq else 0
    

def solution() -> None:
    dq = Deque()

    for i in range(n):
        cmd = cmds[i]
        if cmd == 'push_front':
            dq.push_front(nums[i])
        elif cmd == 'push_back':
            dq.push_back(nums[i])
        elif cmd == 'pop_front':
            print(dq.pop_front())
        elif cmd == 'pop_back':
            print(dq.pop_back())
        elif cmd == 'size':
            print(dq.size())
        elif cmd == 'empty':
            print(dq.empty())
        elif cmd == 'front':
            print(dq.front())
        elif cmd == 'back':
            print(dq.back())

solution()

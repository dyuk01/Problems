# from collections import deque
from typing import List

n = int(input())
commands = []
values = []

for _ in range(n):
    lines = input().split()
    commands.append(lines[0])
    if lines[0] == "push":
        values.append(int(lines[1]))
    else:
        values.append(0)

class Queue:

    queue: List[int]

    def __init__(self):
        self.queue = []
    
    
    def empty(self) -> int:
        return int(not self.queue)


    def size(self) -> int:
        return len(self.queue)


    def push(self, a: int) -> None:
        self.queue.append(a)
    

    def pop(self) -> int:
        return self.queue.pop(0) if not self.empty() else 0


    def front(self) -> int:
        return self.queue[0] if not self.empty() else 0
    

def solution() -> None:
    q = Queue()
    for i in range(n):
        cmd = commands[i]
        if cmd == "push":
            q.push(values[i])
        elif cmd == "pop":
            print(q.pop())
        elif cmd == "size":
            print(q.size())
        elif cmd == "empty":
            print(q.empty())
        elif cmd == "front":
            print(q.front())


solution()

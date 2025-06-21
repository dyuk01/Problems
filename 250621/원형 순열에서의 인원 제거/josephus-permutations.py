from typing import List

n, k = map(int, input().split())

class Queue:
    def __init__(self):
        self.queue = []

    def empty(self) -> bool:
        return not self.queue

    def size(self) -> int:
        return len(self.queue)

    def push(self, val) -> None:
        self.queue.append(val)

    def pop(self) -> int:
        return self.queue.pop(0) if not self.empty() else 0

    def front(self) -> int:
        return self.queue[0] if not self.empty() else 0

def solution() -> List[int]:
    queue = Queue()
    for i in range(1, n + 1):
        queue.push(i)

    res = []
    while not queue.empty():
        for _ in range(k - 1): 
            queue.push(queue.pop())
        res.append(queue.pop())

    return res

print(' '.join(map(str, solution())))

from typing import List

n, k = map(int, input().split())

# Please write your code here.
# Removes k - 1'th push element

class Queue:

    queue: List[int]

    def __init__(self):
        self.queue = []
    

    def empty(self) -> bool:
        return not self.queue
    

    def push(self, val: int) -> None:
        self.queue.append(val)
    

    def pop(self) -> int:
        return self.queue.pop(0)


def solution() -> List[int]:
    queue = Queue()
    for i in range(1, n+1):
        queue.push(i)

    res = []
    while not queue.empty():
        for _ in range(k-1):
            queue.push(queue.pop())
        res.append(queue.pop())
    
    return res

print(' '.join(map(str, solution())))

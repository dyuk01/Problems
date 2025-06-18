n = int(input())
command = []
value = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class Stack:
    def __init__(self) -> None:
        self.items = []
    

    def push(self, item):
        self.items.append(item)
    
    
    def pop(self):
        if self.empty():
            return False
        return self.items.pop()
    

    def size(self) -> int:
        return len(self.items)
    

    def empty(self) -> int:
        if len(self.items) == 0:
            return 1
        return 0
    

    def top(self):
        return self.items[-1]
    

stack = Stack()

for i in range(n):
    if command[i] == "push":
        stack.push(value[i])
    elif command[i] == "pop":
        print(stack.pop())
    elif command[i] == "size":
        print(stack.size())
    elif command[i] == "empty":
        print(stack.empty())
    else:
        print(stack.top())

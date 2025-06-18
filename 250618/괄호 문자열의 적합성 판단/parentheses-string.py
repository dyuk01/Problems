str = input()

# Please write your code here.
class Stack:
    def __init__(self) -> None:
        self.stack = []
    

    def push(self, v: str) -> None:
        self.stack.append(v)
    

    def pop(self) -> str:
        return self.stack.pop() if not self.empty() else ""
    

    def size(self) -> int:
        return len(self.stack)
    
    
    def empty(self) -> bool:
        return self.size() == 0
    

    def peek(self) -> str:
        return self.stack[-1] if not self.empty() else ""
    

    def print_stack(self) -> str:
        return ''.join(self.stack)


def solution() -> bool:
    stack = Stack()

    for c in str:
        # stack.print_stack()
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.empty() or stack.peek() != "(":
                return False
            # if stack.peek() != "(" or stack.empty():
            #     return False
            stack.pop()
    
    return stack.empty()


if solution():
    print("Yes")
else:
    print("No")
        
# str = input()

# # Please write your code here.
# # class Stack:
# #     def __init__(self) -> None:
# #         self.stack = []
    

# #     def push(self, v: str) -> None:
# #         self.stack.append(v)
    

# #     def pop(self) -> str:
# #         return self.stack.pop() if not self.empty() else ""
    

# #     def size(self) -> int:
# #         return len(self.stack)
    
    
# #     def empty(self) -> bool:
# #         return self.size() == 0
    

# #     def peek(self) -> str:
# #         return self.stack[-1] if not self.empty() else ""
    

# #     def print_stack(self) -> str:
# #         return ''.join(self.stack)


# # def solution() -> bool:
# #     stack = Stack()

# #     for c in str:
# #         # stack.print_stack()
# #         if c == "(":
# #             stack.push(c)
# #         elif c == ")":
# #             if stack.empty() or stack.peek() != "(":
# #                 return False
# #             stack.pop()
    
# #     return stack.empty()


# # if solution():
# #     print("Yes")
# # else:
# #     print("No")


# def solution() -> bool:

        


str = input()

def solution() -> bool:
    stack = []
    for p in str:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return len(stack) == 0

if solution():
    print("Yes")
else:
    print("No")

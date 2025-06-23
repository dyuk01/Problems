from typing import List

arr = input()

# # Please write your code here.
# class Stack:

#     stack: List[str]

#     def __init__(self):
#         self.stack = []
    

#     def empty(self) -> bool:
#         return not self.stack
    

#     def push(self, val) -> None:
#         self.stack.append(val)
    

#     def pop(self) -> None:
#         self.stack.pop(-1)
    

# def solution() -> str:
#     stack = Stack()
#     for s in arr:
#         if s == "(":
#             stack.push("(")
#         elif s == ")":
#             if stack.empty():
#                 return "No"
#             stack.pop()
    
#     return "Yes" if stack.empty() else "No"

# print(solution())

def solution() -> str:
    res = []
    for s in arr:
        if s == "(":
            res.append("(")
        elif s == ")":
            if len(res) == 0:
                return "No"
            res.pop(-1)
    
    return "Yes" if len(res) == 0 else "No"

print(solution())

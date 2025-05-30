# n, m = map(int, input().split())
# s = input()

# commands = []
# for _ in range(m):
#     cmd = input().split()
#     if len(cmd) == 1:
#         commands.append((cmd[0],))
#     else:
#         commands.append((cmd[0], cmd[1]))

# # Please write your code here.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.curr = None


#     def left(self):
#         if self.curr == self.head:
#             return
#         self.curr = self.curr.prev


#     def right(self):
#         if self.curr == self.tail:
#             return
#         self.curr = self.curr.next
    

#     def delete(self):
#         # Empty -> pass
#         if self.curr == self.tail:
#             return

#         # Delete last node
#         if self.curr.next == self.tail:
#             self.tail.prev = None
#             self.curr.next = None
#             self.curr = self.tail

#         # Delete middle node
#         else:
#             self.curr.next.next.prev = self.curr
#             self.curr.next = self.curr.next.next
#             self.curr.next.next = None
#             self.curr.next.prev = None


#     def push_back(self, c):
#         new_node = Node(c)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             self.curr = new_node
#             return
        
#         self.tail.next = new_node
#         new_node.prev = self.tail
#         self.tail = new_node
#         self.curr = self.tail


#     def insert(self, c):
#         new_node = Node(c)

#         if self.curr != self.tail:
#             # Add as middle
#             self.curr.next.prev = new_node
#             new_node.next = self.curr.next
#             new_node.prev = self.curr
#             self.curr.next = new_node
#         else:
#             # Add as tail
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
        
#         if self.curr != None:
#             self.curr = self.curr.next
    

#     def print_list(self):
#         node = self.head
#         while node:
#             print(node.data, end='')
#             node = node.next


# dll = DoubleLinkedList()

# # Initialize linked list
# for c in s:
#     dll.push_back(c)

# # Follow the directions
# for i in range(m):
#     direction = commands[i][0]
#     if direction == 'L':
#         dll.left()
#     elif direction == 'R':
#         dll.right()
#     elif direction == 'P':
#         dll.insert(commands[i][1])
#     else:
#         dll.delete()

# dll.print_list()
    
from typing import Optional

n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0], ""))
    else:
        commands.append((cmd[0], cmd[1]))


class Node:
    def __init__(self, data: str):
        self.data = data
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class DLL:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def begin(self) -> Node:
        return self.head

    def end(self) -> Node:
        return self.tail

    def push_back(self, data: str) -> None:
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def move_left(self, it: Node) -> Optional[Node]:
        if it is not self.head:
            return it.prev
    
    def move_right(self, it: Node) -> Node:
        if it is not self.tail:
            return it.next
    
    def remove(self, it: Node) -> None:
        # Nothing to delete at tail.
        if it == self.tail:
            return
        
        # If removing the tail, just pop back.
        if it.next == self.tail:
            self.tail = it
            self.tail.next = None
            return
        
        # Redirect.
        temp = it.next.next
        temp.prev = it
        it.next = temp
        
    def insert(self, data: str, it: Optional[Node]) -> Optional[Node]:
        # If inserting at the tail, just push back.        
        if it == self.tail:
            self.push_back(data)
            return self.tail
        
        # Insert in the middle.
        new_node = Node(data)
        it.next.prev = new_node        
        new_node.next = it.next
        new_node.prev = it
        it.next = new_node
        return new_node

    def print(self) -> str:
        answer = ""
        i = self.head
        while i is not None:
            answer += i.data
            i = i.next
        return answer

def solution() -> str:
    dll = DLL()

    # Populate DLL for input s.
    dll.push_back("")
    for i in range(n):
        dll.push_back(s[i])
    
    it = dll.end()
    # Iterate cmds.
    for c, d in commands:
        if c == "L":
            it = dll.move_left(it)
        elif c == "R":
            it = dll.move_right(it)
        elif c == "D":
            dll.remove(it)
        elif c == "P":
            it = dll.insert(d, it)
    
    return dll.print()

# if __name__ == "main":
print(solution())

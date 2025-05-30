# n = int(input())
# command = []
# a = []

# for _ in range(n):
#     line = input().split()
#     command.append(line[0])
#     if line[0] in ["push_front", "push_back"]:
#         a.append(int(line[1]))
#     else:
#         a.append(0)

# # Please write your code here.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.node_num = 0
    
#     def push_front(self, num_data)-> None:
#         new_node = Node(num_data)

#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             new_node.prev = None
#             self.head.prev = new_node
#             self.head = new_node

#         self.node_num += 1
    
#     def push_back(self, num_data)-> None:
#         new_node = Node(num_data)

#         if self.tail == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = None
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
        
#         self.node_num += 1

    
#     def pop_front(self)-> int:
#         if self.head == None:
#             return -1
        
#         delete_node_data = self.head.data
#         if self.head == self.tail:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
        
#         self.node_num -= 1
#         return delete_node_data


#     def pop_back(self)-> int:
#         if self.tail is None:
#             return -1
        
#         delete_node_data = self.tail.data
#         if self.head == self.tail:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
        
#         self.node_num -= 1
#         return delete_node_data
    
#     def size(self)-> int:
#         return self.node_num
    
#     def empty(self)-> int:
#         return 1 if self.node_num == 0 else 0
    
#     def front(self)-> int:
#         return self.head.data
    
#     def back(self)-> int:
#         return self.tail.data

# l = DoubleLinkedList()
# for i in range(n):
#     cmd = command[i]
#     num = a[i]
#     if cmd == "push_front":
#         l.push_front(num)
#     elif cmd == "push_back":
#         l.push_back(num)
#     elif cmd == "pop_front":
#         print(l.pop_front())
#     elif cmd == "pop_back":
#         print(l.pop_back())
#     elif cmd == "size":
#         print(l.size())
#     elif cmd == "empty":
#         print(l.empty())
#     elif cmd == "front":
#         print(l.front())
#     else:
#         print(l.back())

from typing import Optional

n = int(input())
command = []
a = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        a.append(int(line[1]))
    else:
        a.append(0)

class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.next: Optional['Node'] = None
        self.prev: Optional['Node'] = None

class DLL:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.s = 0
        
    def push_front(self, A: int) -> None:
        new_node = Node(A)
        new_node.next = self.head
        if self.s == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.s += 1

    def push_back(self, A: int) -> None:
        new_node = Node(A)
        new_node.prev = self.tail
        if self.s == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.s += 1

    def pop_front(self) -> int:
        if self.s == 0:
            return 0
        
        data = self.front()
        if self.s == 1:    
            self.head = None
            self.tail = None
        else:
            front = self.head
            self.head = front.next
            self.head.prev = None
            front.next = None
        self.s -= 1
        return data
        
    def pop_back(self) -> int:
        if self.s == 0:
            return 0
        
        data = self.back()
        if self.s == 1:
            self.head = None
            self.tail = None
        else:
            back = self.tail
            self.tail = back.prev
            self.tail.next = None
            back.prev = None
        self.s -= 1
        return data

    def size(self) -> int:
        return self.s

    def empty(self) -> int:
        return 0 if self.s else 1

    def front(self) -> int:
        return self.head.data if self.head else 0

    def back(self) -> int:
        return self.tail.data if self.tail else 0

def solution(n) -> None:
    dll = DLL()

    for i in range(n):
        cmd = command[i]
        n = a[i]

        if cmd == "push_front":
            dll.push_front(n)
        elif cmd == "push_back":
            dll.push_back(n)
        elif cmd == "pop_front":
            print(dll.pop_front())
        elif cmd == "pop_back":
            print(dll.pop_back())
        elif cmd == "size":
            print(dll.size())
        elif cmd == "empty":
            print(dll.empty())
        elif cmd == "front":
            print(dll.front())
        elif cmd == "back":
            print(dll.back())

solution(n)

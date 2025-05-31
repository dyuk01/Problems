n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

# Please write your code here.
from typing import Optional

class Partition:
    def __init__(self):
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Optional[Partition] = None
        self.next: Optional[Partition] = None

class DLL:
    def __init__(self, s):
        curr_part = Partition()
        self.head = curr_part
        self.tail = curr_part

        for ch in s:
            new_node = Node(ch)
            new_part = Partition()
            new_node.next = new_part
            new_part.prev = new_node

            new_node.prev = self.tail
            self.tail.next = new_node

            self.tail = new_part
        
    
    def left(self, cursor):
        if cursor != self.head:
            return cursor.prev.prev
        return cursor
        
    
    def right(self, cursor):
        if cursor != self.tail:
            return cursor.next.next
        return cursor


    def delete(self, cursor):
        if cursor == self.tail:
            return cursor

        if cursor == self.head:
            # Delete first node
            self.head = cursor.next.next
            self.head.prev.next = None
            self.head.prev = None
            return self.head

        if cursor.next.next == self.tail:
            self.tail = cursor
            self.tail.next.prev = None
            self.tail.next = None
            return self.tail
        
        next_node = cursor.next.next.next
        cursor.next = next_node
        next_node.prev = cursor
        return cursor
        

    def paste(self, c, cursor):
        new_node = Node(c)
        new_part = Partition()
        new_node.next = new_part
        new_part.prev = new_node

        old_next = cursor.next
        new_part.next = old_next
        if old_next:
            old_next.prev = new_part
        else:
            self.tail = new_part

        cursor.next = new_node
        new_node.prev = cursor

        return new_part
    

    def print_string(self):
        string = ""
        curr = self.head
        while curr != self.tail:
            string += curr.next.data
            curr = curr.next.next
        return string

        

dll = DLL(s)

cursor = dll.tail
for command in commands:
    cmd = command[0]
    if cmd == 'L':
        cursor = dll.left(cursor)
    elif cmd == 'R':
        cursor = dll.right(cursor)
    elif cmd == 'D':
        cursor = dll.delete(cursor)
    elif cmd == 'P':
        cursor = dll.paste(command[1], cursor)

print(dll.print_string())


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
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Optional[Partition] = None
        self.next: Optional[Partition] = None

class DLL:
    def __init__(self, s):
        self.head = Partition()
        curr_partition = self.head

        for ch in s:
            new_node = Node(ch)
            new_partition = Partition()

            new_node.prev = curr_partition
            curr_partition.next = new_node

            new_partition.prev = new_node
            new_node.next = new_partition

            curr_partition = new_partition
        
        self.tail = curr_partition
        self.curr = self.tail
    
    def left(self):
        if self.curr.prev and self.curr.prev.prev:
            self.curr = self.curr.prev.prev
    
    def right(self):
        if self.curr.next and self.curr.next.next:
            self.curr = self.curr.next.next
    
    def delete(self):
        if not self.curr.next:
            return
        
        node = self.curr.next
        next_partition = node.next

        if next_partition == self.tail:
            # Delete last node
            self.curr.next = None
            self.tail = self.curr
        elif self.curr == self.head:
            # Delete first node
            if next_partition and next_partition.next:
                self.curr.next = next_partition.next
                next_partition.next.prev = self.curr
            else:
                self.curr.next = None
        else:
            # Delete middle node
            self.curr.next = next_partition
            if next_partition:
                next_partition.prev = self.curr


    def paste(self, c):
        new_node = Node(c)
        new_partition = Partition()

        # Insert the new node and partition
        old_next = self.curr.next
        
        # Connect current partition to new node
        self.curr.next = new_node
        new_node.prev = self.curr
        
        # Connect new node to new partition
        new_node.next = new_partition
        new_partition.prev = new_node
        
        # Connect new partition to what was originally next
        new_partition.next = old_next
        if old_next:
            old_next.prev = new_partition
        else:
            # If we're at the end, update tail
            self.tail = new_partition

        # Move cursor to the new partition
        self.curr = new_partition
    
    def print_string(self):
        res = []
        node = self.head.next
        while node and isinstance(node, Node):
            res.append(node.data)
            if node.next:
                node = node.next.next
            else:
                break
        return ''.join(res)

dll = DLL(s)

for command in commands:
    cmd = command[0]
    if cmd == 'L':
        dll.left()
    elif cmd == 'R':
        dll.right()
    elif cmd == 'D':
        dll.delete()
    elif cmd == 'P':
        dll.paste(command[1])

print(dll.print_string())
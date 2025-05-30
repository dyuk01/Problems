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
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr_node = None


    def left(self, curr_node):
        if curr_node.prev == None:
            continue
        else:
            curr_node = curr_node.prev


    def right(self, curr_node):
        if curr_node.next == None:
            continue
        else:
            curr_node = curr_node.next
    

    def delete(self, curr_node):
        # Empty -> pass
        if curr_node.next == None:
            continue
        else:
            # Last node
            if curr_node.next.next == None:
                curr_node.next.prev = None
                curr_node.prev = None
            else:

            

    def paste(self): 
        pass
        
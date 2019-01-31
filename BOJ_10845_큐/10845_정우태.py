class Node:
    elem = None
    prev = None
    next = None
    def __init__(self, elem):
        self.elem = elem
    def get_elem(self):
        return self.elem
    def set_prev(self, node):
        self.prev = node
    def set_next(self, node):
        self.next = node
    def get_prev(self):
        return self.prev
    def get_next(self):
        return self.next

class Queue:
    FRONT = None
    BACK = None
    size = None
    def __init__(self):
        self.size = 0
        self.FRONT = None
        self.BACK = None
    def push(self, node):
        if self.size == 0:
            self.FRONT = node
            self.BACK = node
        else:
            temp = self.BACK
            node.set_prev(temp)
            temp.set_next(node)
            self.BACK = node
        self.size += 1
    def pop(self):
        if self.FRONT is None:
            return -1
        else :
            temp = self.FRONT
            self.FRONT = temp.get_next()
            #temp.set_next(self.FRONT.get_next())
            result = temp.get_elem()
            self.size -= 1
            return result
    def front(self):
        if self.size == 0:
            return -1
        return self.FRONT.get_elem()
    def back(self):
        if self.size == 0:
            return -1
        return self.BACK.get_elem()
    def get_size(self):
        return self.size
    def empty(self):
        size = self.size
        if size == 0:
            return 1
        else:
            return 0

N = int(input())
q = Queue()
for i in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        q.push(Node(cmd[1]))
    elif cmd[0] == "pop":
        print(q.pop())
    elif cmd[0] == "size":
        print(str(q.get_size()))
    elif cmd[0] == "empty":
        print(q.empty())
    elif cmd[0] == "front":
        print(q.front())
    else:
        print(q.back())

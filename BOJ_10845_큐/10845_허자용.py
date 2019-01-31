class Node:
    count = 0
    def __init__(self, value):
        self.value = value
        Node.count += 1
    def setprev(self, prev):
        self.prev = prev
    def setnext(self, next):
        self.next = next


T = int(input())

for i in range(T):
    text = input()
    if text[:4] == "push":
        pushvalue = int(text[5:])
        if not(Node.count):
            head = Node(pushvalue)
            tail = head
        else:
            newest = Node(pushvalue)
            newest.setprev(tail)
            tail.setnext(newest)
            tail = newest

    elif text == "pop":
        if not(Node.count):
            print(-1)
        else:
            print(head.value)
            Node.count -= 1
            if Node.count:
                head = head.next

    elif text == "size":
        print(Node.count)
        
    elif text == "empty":
        print(int(not(Node.count)))
        
    elif text == "front":
        if not(Node.count):
            print(-1)
        else:
            print(head.value)
            
    elif text == "back":
        if not(Node.count):
            print(-1)
        else:
            print(tail.value)

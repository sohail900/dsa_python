"""STACK USING LINKED LIST"""

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next = next

class Stack:
    def __init__(self,head=None):
        self.head = head
        self.size = 0
    def isEmpty(self):
        return self.head is None
    def push(self,data):
        node = Node(data,self.head)
        self.head = node
        self.size += 1
    def pop(self):
        if self.isEmpty() is not None:
            item = self.head.data
            self.head = self.head.next
            self.size -= 1 
            return item
        raise IndexError("Stack is empty")
    def peek(self):
        if self.isEmpty() is not None:
            item = self.head.data
            return item
        raise IndexError("Stack is empty")
    def checkSize(self):
        if self.isEmpty() is not None:
            size = self.size
            return size
        raise IndexError("Stack is empty")

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(f"Stack size is  {s1.checkSize()}")
print(f"Top Element is {s1.peek()}")
print(f'Remove Element is {s1.pop()}')
print(f"Top Element is {s1.peek()}")
print(f"Stack size is  {s1.checkSize()}")

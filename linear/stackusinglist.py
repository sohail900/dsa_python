"""STACK LINEAR DATA STRUCTURE"""
class Stack:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return len(self.data) == 0
    def push(self,item):
        self.data.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.data.pop()
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.data[-1]
    def size(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return len(self.data)
s1 = Stack()
s1.push(20)
s1.push(30)
s1.push(40)
print(f'Top Element is {s1.peek()}')
print(f'Size of Stack is {s1.size()}')
s1.pop()
print(f'Top Element is {s1.peek()}')
print(f'Size of Stack is {s1.size()}')

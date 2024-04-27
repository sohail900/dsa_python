"""EXTENDED LIST USING CLASS"""
class Stack(list): #extend list class
    def isEmpty(self):
        return len(self) == 0 
    def push(self,item):
          self.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack Empty")
        else:
            return super().pop()
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack Empty")
        else:
            return self[-1]
    def insert(self):
        raise AttributeError("'Insert' method is not working with Stack!!!")
s2 = Stack()
s2.push(20)
s2.push(30)
s2.push(40)
s2.push(50)
print(f'Top Element is {s2.peek()}')
s2.pop()
print(f'Top Element is {s2.peek()}')
s2.insert()



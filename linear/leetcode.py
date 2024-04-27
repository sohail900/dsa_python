"""SOLVE QUESTION"""
# Q1: Find max value in Linked List and replace them to new value
# Q2: Find Odd numbers and return sum of Odd numbers.
# Q3: Reverse Linked List
# Q4: Convert this M*y*/n*a*m*e*i*s*/s*o*h*a*i*l into (My Name is Sohail) 

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head
    def isEmpty(self):
        return self.head is None
    def new_node(self,data):
        node = Node(data,self.head)
        self.head = node
    def replace_max(self,data):
        if self.isEmpty():
            print("Not Found")
            return
        temp = self.head
        max = temp 
        while temp is not None:
            if temp.data > max.data:
                max = temp 
            temp = temp.next
        max.data = data
    def sum_of_odd(self):
        if self.isEmpty():
            print("Not Found")
            return
        temp = self.head
        result = 0
        while temp is not None:
            if temp.data % 2 != 0:
                result = temp.data + result
            temp = temp.next
        print("\n","Sum of ODD " , result)
    def reverse(self):
        if self.isEmpty():
            print("Not Found")
            return
        curr_node = self.head
        prev_node = None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node 
            curr_node = next_node
        self.head = prev_node
    def create_new_sentence(self):
        if self.isEmpty():
            print("Not Found")
            return
        temp = self.head
        while temp is not None:
            if temp.data == "*" or temp.data == "/":
                temp.data = " "
                if temp.next.data == '*' or temp.next.data == '/':
                    toUpper = temp.next.next.data.upper()
                    temp.next = temp.next.next
                    temp.next.data = toUpper
            elif temp.data == '&':
                toUpper = temp.next.data.upper()
                temp = temp.next
                temp.data = toUpper
            temp = temp.next
    def traverse(self):
        if self.isEmpty():
            print("Not Found") 
            return
        temp = self.head
        while temp is not None:
            print(temp.data,end="")
            temp = temp.next 

sll = SinglyLinkedList()
# &,h,e,l,l,o,*,/,w,o,r,l,d,/,*,h,a,/,*,h,a convert this into
# Hello World Ha Ha
sll.new_node("a")
sll.new_node("h")
sll.new_node("*")
sll.new_node("/")
sll.new_node("a")
sll.new_node("h")
sll.new_node("*")
sll.new_node("/")
sll.new_node("d")
sll.new_node("l")
sll.new_node("r")
sll.new_node("o")
sll.new_node("w")
sll.new_node("/")
sll.new_node("*")
sll.new_node("o")
sll.new_node("l")
sll.new_node("l")
sll.new_node("e")
sll.new_node("h")
sll.new_node("&")
sll.traverse()
sll.create_new_sentence()
sll.traverse()
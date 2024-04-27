"""Doubly Linked List"""
# Reverse and Forward traversal
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    def __init__(self,head=None):
        self.head = head
    def isEmpty(self):
        return self.head is None
    def insert_at_first(self,data):
        if self.isEmpty():
            self.head = Node(data,self.head,None)#
            return 
        temp = self.head
        self.head = Node(data,temp,None)
        self.head.next.prev = self.head  
    def insert_at_end(self,data):
        if self.isEmpty():
            self.head = Node(data)
            return
        temp = self.head
        while temp is not None:
            if temp.next is None:
                temp.next = Node(data,None,temp)
                break
            temp=temp.next
    def search(self,search_item):
        if self.isEmpty():
            return None
        temp  = self.head
        while temp is not None:
            if(temp.data == search_item):
                print("data found" , temp.data)
                return temp
            temp = temp.next
    def insert_at_position(self,data,position):
        if self.isEmpty():
            self.head = Node(data)
            return
        temp = self.head
        while temp is not None:
            if temp == position:
                node = Node(data,temp.next,temp)
                temp.next = node
                if node.next is not None:
                    node.next.prev = node
                break
            temp = temp.next
    def delete_at_first(self):
        if self.isEmpty():
            return None
        temp = self.head
        self.head = temp.next
        self.head.prev = None
    def delete_at_last(self):
        if self.isEmpty():
            return None
        temp = self.head
        while temp is not None:
            if temp.next is None:
                temp.prev.next = None
                temp.prev = None
                break
            temp = temp.next
    def delete_position(self,search_item):
        if self.isEmpty():
            return None
        temp = self.head
        while temp is not None:
            if temp == search_item:
                temp.next = temp.next.next
                temp.next.prev = temp
                break
            temp = temp.next 
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
            
dll = DoublyLinkedList() #create instance object
dll.insert_at_first(20)
dll.insert_at_first(10)
dll.delete_at_first()
dll.search(5)
dll.insert_at_end(30)
dll.insert_at_position(25,dll.search(20))
dll.insert_at_position(35,dll.search(30))
dll.insert_at_end(40)
dll.delete_at_last()
dll.display()
dll.delete_position(dll.search(25))
dll.display()
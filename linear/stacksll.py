"""STACK USING SINGLY LINKED LIST"""
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head
    def isEmpty(self):
        return self.head is None
    def insert_at_first(self,data):
        node = Node(data,self.head)
        self.head = node
    def insert_at_end(self,data):
        if self.isEmpty():
            node = Node(data,self.head)
            self.head = node
        else:
            temp = self.head
            while temp is not None:
                if temp.next is None:
                    node = Node(data,None)
                    temp.next = node
                    break
                temp=temp.next
    def delete_at_first(self):
        if self.isEmpty():
            raise IndexError("Node is Empty")
        else:
            value = self.head.data
            self.head = self.head.next
            return value
    def delete_at_end(self):
        if self.isEmpty():
            raise IndexError("Node is Empty")
        else:
            temp = self.head
            while temp is not None:
                if temp.next.next is None:
                    temp.next = None
                    break
                temp = temp.next
    def traverse(self):
        if self.isEmpty():
            raise IndexError("Node is Empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end=" ")
                temp = temp.next
                
                
            
                    
      

            
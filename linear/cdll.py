"""CIRCULAR DOUBLY LINKED LIST"""

class Node:
	def __init__(self,data=None,next=None,prev=None):
			self.data = data
			self.next = next
			self.prev = prev
class CircularLinkedList:
    def __init__(self,head=None):
        self.head = head
    def isEmpty(self):
        return self.head is None
    def insert_at_first(self,data):
        node = Node(data)
        if self.isEmpty():
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
        self.head = node
    def insert_at_end(self,data):
        node = Node(data)
        if self.isEmpty():
            node.next = node
            node.prev = node
            return
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
    def search(self,search_item):
        if self.isEmpty():
            return print("Not Found")
        temp = self.head
        if temp.data == search_item:
            print(temp.data)
            return temp
        next_node = temp.next
        while next_node != self.head:
            if next_node.data == search_item:
                 print(next_node.data)
                 return next_node
            next_node = next_node.next
    def insert_after(self,data,search_node):
        if self.isEmpty():
             return print("Not Found")
        node = Node(data)
        node.prev = search_node
        search_node.next.prev = node
        node.next = search_node.next
        search_node.next = node
    def delete_at_first(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
                return 
            temp = self.head
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.head = temp.next
    def delete_at_last(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
                return
            temp = self.head
            temp.prev.prev.next = self.head
            temp.prev = temp.prev.prev 
    def traverse(self):
        if self.isEmpty():
             return print("Node Empty")
        temp = self.head
        if temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
            while temp != self.head:
                print(temp.data,end=" ")
                temp = temp.next
            
cll = CircularLinkedList()
cll.insert_at_first(5)
cll.insert_at_first(6)
cll.insert_at_first(6)
cll.insert_at_end(8)
cll.insert_at_end(9)
cll.search(8)
cll.insert_after(30,cll.search(9))
cll.traverse()
cll.delete_at_first()
cll.traverse()
cll.delete_at_last()
cll.traverse()
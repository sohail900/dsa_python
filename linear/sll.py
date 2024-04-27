""" SINGLY LIST LINKED """
class Node:
    def __init__(self, item=None,next=None):
        self.item= item
        self.next = next
        
## single list linked
class SinglyListLinked:
    def __init__(self):
        self.head = None #referred to first node
    #check if node is empty or not.
    def isEmpty(self):
        return self.head is None #return true if head is None
    def insert_at_start(self,data): 
         node=Node(data,self.head) #create first node
         self.head = node #create first referred node
    def insert_at_end(self,data): 
        node=Node(data)
        temp = self.head
        if self.isEmpty():
            self.head = node
            return
        while temp is not None:
            if temp.next is None:
                temp.next = node
                break
            temp = temp.next
    def search(self,data):
        temp = self.head
        while temp is not None:
            if temp.item == data:
                print(temp.item)
                return temp
            temp = temp.next
        return None
    def insert_after(self,data,after_item):
        if after_item is not None:
            temp = Node(data,after_item.next)
            after_item.next = temp
            return True
        None
    def delete_at_start(self):
        if self.isEmpty():
            return None
        temp = self.head
        temp.next = temp.next.next
    def delete_at_end(self):
        if self.isEmpty():
            return None
        temp = self.head
        while temp.next.next is not None: 
            temp = temp.next
        temp.next = None
    def delete_after(self,after_item):
        if after_item is None:
            return None
        temp = self.head
        while temp is not None:
            if temp.next == after_item:
                temp.next = after_item.next
                return
            temp = temp.next
    def display_list(self):
        if self.isEmpty():
            return print("List is empty")
        temp = self.head
        while temp is not None:
            print(temp.item,end=" -> ")
            temp = temp.next
    def __iter__(self): #create a iterable object
        temp = self.head
        while temp is not None:
            yield temp.item # return single value at a time and maintain function's state
            temp = temp.next
        

sll = SinglyListLinked()


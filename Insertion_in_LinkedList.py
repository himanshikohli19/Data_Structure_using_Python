'''
Insertion in Linked List can be done is 3 ways:
1. At the Beginning of the List
2. After a node
3. At a end of the list
'''
#a Node Class
class Node:
    def __init__(self ,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self): #for head
        self.head=None

    def pushAtStart(self,new_data): #function to insert node at beginning
        new_node = Node(new_data) #creating new node and add new_data
        new_node.next = self.head #pointing next of the new_node to head node
        self.head = new_node #assigning new_node as head

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node should be the part of linked list")
            return
        
        new_node=Node(new_data)#creating new node and add new_data
        new_node.next=prev_node.next #pointing next of the new_node to next of prev_node
        prev_node.next=new_node #next of prev_node pointing to new_node

    def append(self,new_data):
        new_node=Node(new_data) #creating new node and add new_data

        if self.head is None: #if list is empty, then point head to new_node 
            self.head = new_node
            return
        
        #traversing the list till Null
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node #next of last node will point to new_node

    def printList(self): #for printing the whole linked list
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.pushAtStart(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.pushAtStart(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
 
    print ('Created linked list is:')
    llist.printList()
        

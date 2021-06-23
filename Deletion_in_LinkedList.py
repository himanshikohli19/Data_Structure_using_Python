'''
Deletion of an element/node in a Linked List
To delete a node from the linked list, we need to do the following steps. 
1) Find the previous node of the node to be deleted. 
2) Change the next of the previous node. 
3) Free memory for the node to be deleted.
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def deleteNode(self,key):
        temp=self.head
        # If head node itself holds the key to be deleted
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=none
                return
        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev=temp
            temp=temp.next
        # if key was not present in linked list
        if(temp==None):
            return
        #unlink the node from LL
        prev.next=temp.next
        temp=None
        

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
 
print ("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print ("\nLinked List after Deletion of 1:")
llist.printList()

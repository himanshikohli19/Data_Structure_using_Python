 #Reverse of a linked List 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data): #appending the node to the beginning
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printList(self): #printing the List
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def reverse(self): #reversing the Linked List
        prev=None
        current=self.head
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
            
        
if __name__=='__main__':
    llist=LinkedList()
    llist.push(2)
    llist.push(3)
    llist.push(7)
    llist.push(9)
    llist.push(8)
    llist.push(20)
    print("Original List:")
    llist.printList()
    print("\nReversed List:")
    llist.reverse()
    llist.printList()

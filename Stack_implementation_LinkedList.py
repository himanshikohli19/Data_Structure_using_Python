#IMPLEMENTING STACK VIA LINKED LIST
'''
1 -> 7 -> 8 -> 6 -> 4
'''
#a Node Class
class Node:
    def __init__(self ,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self): #for head
        self.head=None

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
        
    #adding node at the end of the Linked List (TOP)
    def push(self,new_data):
        new_node=Node(new_data) #creating new node and add new_data
        if self.isEmpty(): #if list is empty, then point head to new_node 
            self.head = new_node
            return 
        #traversing the list till Null
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node #next of last node will point to new_node

#delete/POP top node out of the stack
# Function to remove the last node of the linked list
    def pop(self):
        if self.isEmpty():
            return None
        if self.head.next == None:
            self.head = None
            return None
        self.second_last = self.head
        while(self.second_last.next.next):
            self.second_last = self.second_last.next
        self.second_last.next = None
        return 
        
        

    def printList(self): #for printing the whole linked list
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

# Code execution starts here
if __name__=='__main__':

    llist = LinkedList()
 
    llist.push(1)
    llist.push(7)
    llist.push(8)
    llist.push(6)
    llist.push(4)
 
    print ('Created linked list is:')
    llist.printList()
    print("POP out the TOP element")
    llist.pop()
    print("New List:")
    llist.printList()

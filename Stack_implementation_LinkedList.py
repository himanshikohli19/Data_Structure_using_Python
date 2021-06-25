#IMPLEMENTING STACK VIA LINKED LIST
'''
1 -> 7 -> 8 -> 6 -> 4
'''
#a Node Class
class Node:
    def __init__(self ,data):
        self.data=data
        self.next=None

class Stack:
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
        second_last = self.head
        while(second_last.next.next):
            second_last = second_last.next
        second_last.next = None
        return 
        
        

    def printList(self): #for printing the whole linked list
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

# Code execution starts here
if __name__=='__main__':

    s = Stack()
 
    s.push(1)
    s.push(7)
    s.push(8)
    s.push(6)
    s.push(4)
 
    print ('Created linked list is:')
    s.printList()
    print("POP out the TOP element")
    s.pop()
    print("New List:")
    s.printList()

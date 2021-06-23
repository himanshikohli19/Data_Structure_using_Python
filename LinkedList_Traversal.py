#Linked List Traversal and print

class Node: #Node class created
    def __init__(self,data): #function to initialize the Node-->data,next
        self.data=data
        self.next=None
        
#LinkedList class contains node object        
class LinkedList: #function to initialize head
    def __init__(self):
        self.head=None

    def printList(self): #to print the linked list
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

#driver code (main function)
if __name__ == '__main__':
    llist=LinkedList() #object created for class LinkedList
    llist.head=Node("Test1") #giving content in data part of linked list - head Node
    second=Node("Test2") #giving content in data part of linked list - second Node
    third=Node("Test3") #giving content in data part of linked list - third Node

    llist.head.next=second #linking head to second
    second.next=third #linking second to third
    llist.printList() #calling function printList() 
    

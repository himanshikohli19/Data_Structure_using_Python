#Merge two Sorted Linked List
'''
5->10->15
2->3->20
output: 2-> 3-> 5-> 10 ->15
'''

#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def addToList(self,new_data):
        new_node=Node(new_data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node           

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
def mergeLists(headA, headB):
    dummyNode=Node(0)
    tail=dummyNode
    while True:
        if headA is None:
            tail.next=headB
            break
        if headB is None:
            tail.next=headA
            break
        if headA.data <= headB.data:
            tail.next=headA
            headA=headA.next
        else:
            tail.next=headB
            headB=headB.next
                
        tail=tail.next
            
    return dummyNode.next

# Create 2 lists
listA = LinkedList()
listB = LinkedList()
 
# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)
 
listB.addToList(2)
listB.addToList(3)
listB.addToList(20)
print("List A")
listA.printList()
print("List B")
listB.printList()
# Call the merge function
listA.head = mergeLists(listA.head, listB.head)
 
# Display merged list
print("Merged Linked List is:")
listA.printList()

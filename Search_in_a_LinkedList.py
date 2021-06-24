#Searching in a linked List 
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

    def search(self,ele):
        temp=self.head
        while(temp):
            if(temp.data==ele):
                print("Element",ele,"found")
                break
            temp=temp.next
        
if __name__=='__main__':
    llist=LinkedList()
    llist.push(2)
    llist.push(3)
    llist.push(7)
    llist.push(9)
    llist.push(8)
    llist.push(20)
    llist.search(7)

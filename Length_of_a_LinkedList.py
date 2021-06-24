#Find the length of the Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data): #pushing the node at the beginning of the list
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def countAndPrint(self):
        count=0
        temp=self.head
        while(temp):
            print(temp.data)
            count+=1 #counting the list
            temp=temp.next
        return count

if __name__=='__main__':
    llist=LinkedList()
    llist.push(3)
    llist.push(7)
    llist.push(8)
    llist.push(10)
    llist.push(2)
    llist.push(1)
    llist.push(5)
    print("Length of the Linked List: ",llist.countAndPrint())

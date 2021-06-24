#Implementation of Stack using Python Lists

class Stack:
    def __init__(self):
        self.items=[] #list declaration

    def push(self,item):
        self.items.append(item) #adding item on the top

    def pop(self):
        return self.items.pop() #taking out item from the top

    def isEmpty(self):
        return (self.items==[]) #if list is empty

if __name__=='__main__':
    s=Stack()
    s.push(45)
    s.push(455)
    s.push(458)
    while(not s.isEmpty()):
        print(s.pop())

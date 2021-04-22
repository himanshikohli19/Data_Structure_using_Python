#Linear Search with improved time complexity

#function linear search
def Lsearch(list1,a,s):
    left=0 #start from left(initial position)
    len1=len(list1)
    right=len1-1 #right side of the list(end position)
    pos=-1
    for left in range(0,a):

        if list1[left]==s:
            pos=left
            print("Element found at position: ", pos+1,"in",left+1,"Attempt")
            break
        
        if list1[right]==s:
            pos=right
            print("Element found at position: ", pos+1,"in",len1-right,"Attempt")
            break
        
        left+=1
        right-=1
        pos=0
        
        if pos==-1:
            print("Element not found!")
            
    return -1

#Driver code(main)
list1=[]
a=int(input("Enter the number of elements you want to enter: "))
for i in range(0,a):
    ele=int(input("Enter the element: "))
    list1.append(ele)

s=int(input("Enter the element you want to search for: "))
Lsearch(list1,a,s) #function call


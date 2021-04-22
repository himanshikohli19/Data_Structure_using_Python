#Linear search
#function Lsearch
def Lsearch(list1,a,s):
    for j in range(0,a):
        if list1[j]==s:
            return j
    return -1
#driver code
list1=[]
a=int(input("Enter the number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the element: "))
    list1.append(ele)
print("Here's the sequence of number you entered: ",list1)
s=int(input("Enter the element you want to search for: "))
res=Lsearch(list1,a,s) #function call

if res == -1:
    print("Element not found!")
else:
    print("Element found at position: ",res+1)



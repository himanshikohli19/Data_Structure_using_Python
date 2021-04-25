#Time complexity of O(1)

def Bsearch(list1,l,r,x):
    while l<=r:
        mid=l+(r-1)//2
        if list1[mid]==x:
            return mid
        elif list1[mid]<x:
            l=mid+1
        else:
            r=mid-1
    return -1

#driver code
list1=[1,2,3,4,6,7,9,10,15,17,18,20,22,25,28,31,34,35]
x=10
res=Bsearch(list1,0,len(list1)-1,x)
if res!=-1:
    print("Element is the present at ",res+1)
else:
    print("Element not found")

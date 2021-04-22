#simple Binary search (Recursive binary search)-O(Log N)

#function
def Bsearch(list1,l,r,s):
    if r>=l:
        mid=(l+r)//2
        if list1[mid]==s:
            return mid
        elif list1[mid]>s: #middle term is greater than searched term --> focus on left
            return Bsearch(list1,l,mid-1,s)
        else: #middle term is smaller than searched term--> focus on right
            return Bsearch(list1,mid+1,r,s)
    else:
        return -1
        


#Driver code
list1=[1,2,3,4,5,7,8,9,10,12,15,20]
s=10
res=Bsearch(list1,0,len(list1),s) #function call
if res==-1:
    print("Element not found")
else:
    print("Element found at pos: ",res+1)

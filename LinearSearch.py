# Simple Linear Search using function
def Lsearch(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1

#main code(Driver)
arr=[2,3,5,6,9,10,40]
x=9
n=len(arr)
res=Lsearch(arr,n,x)
if (res==-1):
    print("Element not present")
else:
    print("Element found at index: ",res+1)

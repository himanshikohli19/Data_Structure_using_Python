#BUBBLE SORTING
#with less swaping
def BubbleSort(list1):
    n=len(list1)
    for i in range(n):
        swap=False
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
                swap=True
                
        if swap==False:
            break
        
#driver code
list1=[23,67,81,21,12,45,66,98,11,2,5,9,18]
BubbleSort(list1) #function call
print("sorted array")
for i in range(0,len(list1)):
    print(list1[i])

#INSERTION SORT
#with time complexity: O(nxn)
#with space complexity: O(n)

def InsertionSort(list1):
    for i in range(len(list1)):
        key=list1[i]
        j=i-1
        while ((j>=0) and (key<list1[j])):
            list1[j+1]=list1[j]
            j=j-1
            list1[j+1]=key

    return list1
    
    
#driver code
list1=[34,87,90,12,35,69,52,11,2,7,50]
InsertionSort(list1)
for i in range(len(list1)):
    print(list1[i])
    

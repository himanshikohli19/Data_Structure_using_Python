'''
QUICK SORT
using first element as PIVOT
'''
#This function helps in getting pivot to its correct position and partition sorting
def Partition(start, end, Array):
    pivot_index=start
    pivot=Array[pivot_index]
    while (start<end):
        while start < len(Array) and Array[start] <= pivot:
            start += 1
        while Array[end]>pivot:
            end -= 1
        if (start<end):
            Array[start],Array[end]=Array[end],Array[start]

    Array[end],Array[pivot_index]=Array[pivot_index],Array[end]
    return end

def Quick_Sort(start, end, Array):
    if (start<end):
        loc=Partition(start,end,Array)
        Quick_Sort(start,loc-1,Array)
        Quick_Sort(loc+1,end,Array)

#Driver Code
Array=[12,3,23,45,21,22,2,50,9,32]
print("Original Array: ",Array)
Quick_Sort(0,(len(Array)-1), Array)
print("Sorted Array: ",Array)

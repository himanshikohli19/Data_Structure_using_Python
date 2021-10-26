#Greedy Algorithm
#Job Sequencing with Deadlines

def printJobSequence(arr,t):
    n=len(arr)
    #Job sorting in decreasing order
    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2]<arr[j+1][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    #keeps tract of free time-slots
    result=[False]*t
    #To store result
    job=['-1']*t

    for i in range(len(arr)):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                job[j]=arr[i][0]
                break

    print(job)

#driver code
arr=[['A',2,100],['B',1,19],['C',2,37],['D',1,26],['E',3,17],['F',4,10],]
print("following is the maximum profit scheduling of Jobs: ")
printJobSequence(arr,4)

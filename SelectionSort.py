#Selection sort-find the minimum

A = [6,8,1,4,9,10,0,2,15,78]
for i in range(len(A)):   
    mini = i
    for j in range(i+1, len(A)):
        if A[mini] > A[j]:
            mini = j                    
    A[i], A[mini] = A[mini], A[i] #Swapping
  

print ("Sorted array\n")
for i in range(len(A)):
    print(A[i])

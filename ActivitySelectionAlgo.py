#greedy algorithms
#Activity selection Algo

start_Time=[1,3,0,5,6,8,5,7]
final_Time=[2,4,6,7,9,12,9,10]
n=len(final_Time)
#first activity selected
print("Following activities are selected: ")
i=0
print(i)
for j in range(n):
    if start_Time[j] >= final_Time[i]:
        print(j)
        i=j

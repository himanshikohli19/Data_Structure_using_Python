#Greedy algorithm
#Fractional Knapsack algo...

n=int(input("Enter no. of items: "))
maxwt=int(input("Maximum weight: "))
profit=list(map(int, input("Enter profit value of items: ").split()))
weight=list(map(int, input("Enter weight of items: ").split()))

#Initializing total weight in sack as wt and maximum profit value as max_profit
wt=0
max_profit=0

#Calculating profit value per weight value for objects
ppw = []
for i in range(n):
    ppw.append(profit[i]/weight[i])

#Creating sequence for putting objects in the sack
order=[] #order list contains list index of object in decreasing order of profit value per weight
for i in range(n):
    order.append(ppw.index(max(ppw)))
    ppw[ppw.index(max(ppw))]=0

i=0
#Putting items of higher profit value per weight in sack
print("\nItems in Knapsack: ")
print("Item\tWeight\tProfit Value\tFraction")
while wt!=maxwt:
    if (wt+weight[order[i]])<=maxwt:
        max_profit+=profit[order[i]]
        wt+=weight[order[i]]
        print(order[i]+1,"\t",weight[order[i]],"\t",profit[order[i]])
    else:
        fraction = (maxwt-wt)/weight[order[i]]
        value = profit[order[i]]*fraction
        max_profit+= value
        wt+=(maxwt-wt)
        print(order[i]+1,"\t",weight[order[i]],"\t",value,"\t",fraction)
    i+=1

print("\nMaximum profit = ",max_profit)

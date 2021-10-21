#Greedy algorithm
#0/1 Knapsack algo

def greedy_knapsack(values,weights,capacity):
    n = len(values)
    def score(i) : return values[i]/weights[i]
    items = sorted(range(n)  , key=score , reverse = True)
    sel, value, weight = [],0,0
    for i in items:
        if weight +weights[i] <= capacity:
            sel += [i]
            weight += weights[i]
            value += values [i]
    return sel, value, weight


weights = [4,9,10,20,2,1]
values = [400,1800,3500,4000,1000,200]
capacity = 20

print(greedy_knapsack(values,weights,capacity))

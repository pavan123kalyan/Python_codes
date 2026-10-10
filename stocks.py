#prices= [7, 10, 1, 3, 6, 9, 2]
prices=[8,6,3,2,10]
n=len(prices)
res=0
for i in range(n-1):
    for j in range(i+1, n):
        res=max(res, prices[j]-prices[i])
        #print(res)
print(res)

#Optimal solution
prices=[8,6,3,2,10]
mini= prices[0]
res=0
for i in range(1, n):
    mini=min(mini, prices[i])
    res=max(res, prices[i]-mini)
    print(res)
print(res)
arr=[100,6,60,3,6]
p=list(set(arr))
#p=[3, 6, 60, 100]
p.sort()
rank=1
hm={}
for i in p:
    hm[i]=rank
    rank+=1
print(hm)
res=[]
for i in arr:
    res.append(hm[i])
print(res)

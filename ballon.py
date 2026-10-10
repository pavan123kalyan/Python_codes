n=int(input()) #5
l=list(map(int,input().split())) #25 50 35 100 85
k=int(input())# 225
l.sort()#25,50,35,85,100
total=0
for i in range(n):
    k-=l[i]
    if(k<=0):
        break
    total+=1
print(total)




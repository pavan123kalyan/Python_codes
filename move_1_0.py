p=[0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1]
n=len(p)
i=0
j=n-1
while(i<j):
    if(p[i]==0):
        i+=1
    elif(p[j]==1):
        j-=1
    else:
    #if(p[i]==1 and p[j]==0):
        p[i],p[j]=p[j],p[i]
        i+=1
        j-=1
print(p)
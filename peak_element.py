#Findind Peak element --> TC=O(n)
p=[1,3,5,7,-1,8,9,-1,4,9]
n=len(p)
if(n<=1 or p[0]>p[1]):
    print(0)
if(p[n-2]<p[n-1]):
    print(n-1)
for i in range(n-1):
    if(p[i]<p[i+1]):
        pass
    else:
        print(i)

#Optimal approach -->Binary search ---> T.C=O(logn)

p=[1,3,5,7,-1,8]
n=len(p)
i=0
j=n-2

if(n<=1 or p[0]>p[1]):
    print(0)
if(p[n-2]<p[n-1]):  
    print(n-1)
while(i<=j):
    mid=(i+j)//2
    if(p[mid-1]<p[mid] and p[mid]>p[mid+1]):
        print(mid)
        break
    else:
        if(p[mid]<p[mid+1]):
            i=mid+1
        else:
            j=mid-1

#Approach-1
#T.C : O(n)
n=23
p=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        p.append(i)
if(c==2):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

#Approach-2
#TC: O(sqrt(n))
import math
n=68
p=[]
c=0
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        c+=1
        p.append(i)
        if((n//i!=i)):
            c+=1
            p.append(n//i)
print(p)
if(c==2):
    print(f"{n} is Prime")
else:
    print(str(n)+ " is not a Prime")
    
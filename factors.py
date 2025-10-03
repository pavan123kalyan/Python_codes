#python factors.py   ---> To run
#Approach-1 
#TC: O(n)
n=10
p=[]
for i in range(1,n+1):
    if n%i==0:
        p.append(i)
print(p) #[1, 2, 5, 10]

#Approach-2
#TC: O(sqrt(n))
import math
n=10
p=[]
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        p.append(i)
        if((n//i!=i)):
            p.append(n//i)
p.sort()
print(p) #[1, 2, 5, 10]
# 1) Brute Force
#TC: O(n^3)
l1=[-2,-3,4,-1,-2,1,5,-3]
n=len(l1)
maxi=float('-inf')
for i in range(n):
    for j in range(i,n):
        sum=0
        for k in range(i,j):
            sum+=l1[k]
        maxi=max(sum,maxi)
print("Max Subarray Sum is:",maxi)

#2)Better Approach ,TC: O(n^2)
l1=[-2,-3,4,-1,-2,1,5,-3]
n=len(l1)
maxi=float('-inf')
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=l1[j]
        maxi=max(maxi,sum)
print("Better Approach:",maxi)

# 3) Optimal Approach
#Kadens Algo for maximum Subarray Sum
l=[-2,-3,4,-1,-2,1,5,-3]
p=len(l)
maxi=float('-inf')
sum1=0
for i in range(p):
    sum1+=l[i]
    #print(sum1)
    if(sum1>maxi):
        maxi=sum1
    if(sum1<0):
        sum1=0
print("Maximum Subarray Sum is:",maxi) 


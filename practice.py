#A robot need to reach destination in minimum time. It can move 5 units in 1 second. Given the distance n, find the minimum time required to reach the destination.
n=185
p=n//5
rem=n%5
c=p
#print(c)
if(rem>0 and rem<5):
    c+=1
print(c)
    
#Maximum consecutive ones or zeros in a binary array
s="10110111110101"
c=1
maxi=1
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        c+=1
        maxi=max(maxi,c)
    else:
        c=1
print(maxi)
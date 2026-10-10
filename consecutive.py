#Maximum consecutive ones or zeros in a binary array
l=[1, 1, 0, 1,0,0,0,1,1,1,1] #output: 3
c1,c2=0,0
maxi=0
for i in l:
    if(i==1):
        c1+=1
        c2=0
    else:
        c2+=1
        c1=0
    maxi=max(maxi,c1,c2)
print(maxi)

#other approach
arr = [0, 1, 0, 1, 1, 1, 1]
maxi = 1
count = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        count += 1
    else:
        count = 1
    if count > maxi:
        maxi = count
print(maxi) 
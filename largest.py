#1st largest and 2nd Largest number 
arr=[-5,-10,-2]
largest=arr[0]
s_largest=float('-inf')
for i in range(1,len(arr)):
    if(arr[i]>largest):
        s_largest=largest
        largest=arr[i]
    elif(arr[i]>s_largest and arr[i]!=largest):
        s_largest=arr[i]
print(largest,s_largest,end=" ")
print(" ")


arr=[-2,-5,-20]
largest=arr[0]
for i in range(1,len(arr)):
    if(arr[i]>largest):
        largest=arr[i]
s_largest=float('-inf')
for i in range(1,len(arr)):
    if(arr[i]>s_largest and arr[i]!=largest):
        s_largest=arr[i]

print(largest,s_largest,end=" ")


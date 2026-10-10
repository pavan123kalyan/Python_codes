#Reduce String Using K
#Remove characters that appear k times consecutively.
s = "deeedbbcccbdaa"
k = 3
stack=[]
for i in s:
    if stack and stack[-1][0]==i:
        stack[-1][1]+=1
        if(stack[-1][1]==k):
            stack.pop()
    else:
        stack.append([i,1])
res=""
for i,j in stack:
    res+=i*j
print(res)
print(2500//1000)
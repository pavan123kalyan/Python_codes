#Product of numbers in array ,except that number.
# arr=[3,5,6]
#output: [30,18,15]

# pre=[1,3,15]  
# suff=[30,6,1] 
nums=[3,5,6]
n=len(nums)
pre=[1]*n  #[1,1,1]
suf=[1]*n  #[1,1,1]
for i in range(1,n):
    pre[i]=pre[i-1]*nums[i-1]
for i in range(n-2,-1,-1):
    suf[i]=suf[i+1]*nums[i+1]
res=[]
for i in range(n):
   res.append(pre[i]*suf[i])
print(res)
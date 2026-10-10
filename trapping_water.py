arr=[3, 0, 1, 0, 4, 0, 2]
n=len(arr)
left=[0]*n
right=[0]*n
left[0]=arr[0]
for i in range(1, n):
    left[i]=max(left[i-1], arr[i])
print(left)
right[n-1]=arr[n-1]
for i in range(n-2, -1, -1):
    right[i]=max(right[i+1], arr[i])
print(right)
res=0
for i in range(n):
    res+=min(left[i], right[i])-arr[i]
print(res)
#Brute force solution

#l= [-2, 6, -3, -10, 0, 2] #output: 180
l=[0]
maxi=float('-inf')
for i in range(len(l)):
    pro=1
    for j in range(i, len(l)):
        pro*=l[j]
        maxi=max(maxi, pro)
print(maxi)

#Optimized solution(Kadane's algorithm for maximum product subarray)
arr = [-2, 6, -3, -10, 0, 2] 
maxi = arr[0]
mini = arr[0]
ans = arr[0]
for i in range(1, len(arr)):
    if arr[i] < 0:
        maxi, mini = mini, maxi
    maxi = max(arr[i], maxi * arr[i])
    mini = min(arr[i], mini * arr[i])
    ans = max(ans, maxi)
print(ans)

#Optimal 
arr = [-2, 6, -3, -10, 0, 2]
pref = 1
suff = 1
ans = float('-inf')
n = len(arr)
for i in range(n):
    pref *= arr[i]
    suff *= arr[n-i-1]
    ans = max(ans, pref, suff)
    if pref == 0:
        pref = 1
    if suff == 0:
        suff = 1
print(ans)
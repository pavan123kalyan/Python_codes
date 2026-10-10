#Input:s=abcba,k=2
#Output: 3

s = input().strip()
k = int(input())    
l = 0
maxi = 0
hm = {}
for r in range(len(s)):
    hm[s[r]] = hm.get(s[r], 0) + 1
    print(hm)
    while len(hm) > k:
        hm[s[l]] -= 1
        if hm[s[l]] == 0:
            del hm[s[l]]
        l += 1
    maxi = max(maxi, r - l + 1)
print(maxi)
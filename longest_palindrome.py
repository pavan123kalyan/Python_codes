#Find the length of longest palindrome substring
s="abcczyyzccbczc"
n = len(s)
maxi = 0
for i in range(n):    
    # odd length palindrome
    l = i
    r = i
    while l >= 0 and r < n and s[l] == s[r]:
        maxi = max(maxi, r - l + 1)
        l -= 1
        r += 1
    # even length palindrome
    l = i
    r = i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        maxi = max(maxi, r - l + 1)
        l -= 1
        r += 1
print(maxi)


#Generate longest palindrome substring
s="abcczyyzccbczc"
n = len(s)
maxi = 0
start = 0
for i in range(n): 
    # odd
    l = i
    r = i
    while l >= 0 and r < n and s[l] == s[r]:
        if r - l + 1 > maxi:
            maxi = r - l + 1
            start = l
        l -= 1
        r += 1
    # even
    l = i
    r = i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        if r - l + 1 > maxi:
            maxi = r - l + 1
            start = l
        l -= 1
        r += 1
print(s[start:start + maxi])

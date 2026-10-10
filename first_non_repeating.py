s = "geeksforgeeks"
#Output: 'f'
p=len(s)
for i in range(p):
  c=1
  for j in range(p):
    if(i!=j and s[i]==s[j] ):
      c+=1
  if(c==1):
    print(s[i])
    break

#Approach 2
s="geeksforgeeks"
from collections import Counter
c = Counter(s)
for i in s:
    if c[i] == 1:
        print(i)
        break

#Approach 3
s = "geeksforgeeks"
hm = {}
# count frequency
for i in s:
    hm[i] = hm.get(i,0) + 1
# find first non repeating
for i in s:
    if hm[i] == 1:
        print(i)
        break
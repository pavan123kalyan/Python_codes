s="geeksforgeeks"
n=len(s)
maxi=0
res=""
for i in range(n):
  c=1
  for j in range(n):
    if(i!=j and s[i]==s[j]):
      c+=1
  if(c>maxi):
    maxi=c
    res=s[i]
print(res)

#Approach 2
s="geeksforgeeks"
hm={}
for i in s:
  hm[i]=hm.get(i,0)+1
maxi=0
res=""
for i,j in hm.items():
  if j>maxi:
    maxi=j
    res=i
print(res)

#Approach 3
s = "geeksforgeeks"

hm = {}

for i in s:
    hm[i] = hm.get(i,0) + 1

print(max(hm, key=hm.get))
s = "geeksforgeeks"
#Output: g2 e4 k2 s2 f1 o1 r1
hm={}
s1=""
for i in s:
  if i not in hm:
    hm[i]=1
  else:
    hm[i]+=1
for i,j in hm.items():
	s1+=i+str(j) + " "
print(''.join(s1))

#Approach 2
s = "geeksforgeeks"
#Output: g2 e4 k2 s2 f1 o1 r1
hm={}
s1=""
for i in s:
  hm[i]=hm.get(i,0)+1
print(hm)
for i,j in hm.items():
	s1+=i+str(j) + " "
print(''.join(s1))

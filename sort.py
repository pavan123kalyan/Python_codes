#a1 = [2, 1, 2, 3, 4]
a1=[1,2,2,3,4]
a2 = [2, 1, 2]
hm={}
for i in a1:
    hm[i] = hm.get(i, 0) + 1
l=[]
#follows a2 order
for i in a2:
    if i in hm:
        for j in range(hm[i]):
            l.append(i)
            print(l)
        del hm[i]
print(hm)
#sort remaining elements
rem=[]
for i in hm:
    for j in range(hm[i]):
        rem.append(i)
rem.sort()
for i in rem:
    l.append(i)
print(l)
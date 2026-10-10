s = "ab1z91"
hm={}
for i in s:
    if i not in hm:
        if i.isalpha():
            hm[i]=chr(122-ord('i')+1)
        else:
            hm[i]=9-int(i)
    else:
        hm[i]+=1
print(hm)
                    
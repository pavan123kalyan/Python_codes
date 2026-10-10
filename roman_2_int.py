class Solution:
    def romanToInt(self, s: str) -> int:
        a=[]
        sum=0
        for i in s:
            if(i=="I"):
                a.append(1)
            if(i=="V"):
                a.append(5)
            if(i=="X"):
                a.append(10)
            if(i=="L"):
                a.append(50)
            if(i=="C"):
                a.append(100)
            if(i=="D"):
                a.append(500)
            if(i=="M"):
                a.append(1000)
        for j in range(len(a)):
            if(j!=len(a)-1 and a[j]<a[j+1]):
                a[j+1]=a[j+1]-a[j]
                continue
            sum+=a[j]
        print(sum)
        
             
s = "MCMXCIV"
hm={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
res=0
for i in range(len(s)):
    if(i<len(s)-1 and hm[s[i]]<hm[s[i+1]]):
        res-=hm[s[i]]
    else:
        res+=hm[s[i]]
print(res)
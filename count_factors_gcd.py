a=20
b=0
#Find Gcd
while(b!=0):
    a,b=b,a%b
gcd=a
print(gcd)
#Count factors of GCD
cnt,i=0,1
while(i*i<=gcd):
    if(gcd%i==0):
        cnt+=1
        if(i!=gcd//i):
            cnt+=1
    i+=1
print(cnt)


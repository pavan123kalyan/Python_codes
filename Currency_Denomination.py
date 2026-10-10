amt = 2800
L = [100,200,500,1000]
L.sort(reverse=True)
for i in L:
    cnt=amt//i
    print(i,"-",cnt)
    amt=amt%i
    
#Output:
# 1000 - 2
# 500 - 1
# 200 - 1
# 100 - 1
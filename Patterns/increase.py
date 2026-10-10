n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ") # stay in same line
        if(i!=j):
            print("*",end=" ") # stay in same line
    print()   # move to next line after each row
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ") # stay in same line
        if(i!=j):   
            print("*",end=" ") # stay in same line
    print()   # move to next line after each row
#output:
# 1
# 2 * 2
# 3 * 3 * 3
# 4 * 4 * 4 * 4
# 4 * 4 * 4 * 4
# 3 * 3 * 3
# 2 * 2
# 1
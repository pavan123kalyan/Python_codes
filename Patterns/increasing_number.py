for _ in range(int(input())):
    n=int(input())
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j ,end=" ") # stay in same line
        print()   # move to next line after each row

# 4
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
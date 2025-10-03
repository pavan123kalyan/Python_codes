for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        for j in range(i+1):
            print("*",end="") # stay in same line
        print()   # move to next line after each row

# 3
# *
# **
# ***
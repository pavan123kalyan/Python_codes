# for _ in range(int(input())):
#     n=int(input())
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="") # stay in same line
#         print()   # move to next line after each row

# 3
# *
# **
# ***
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
        if(j!=i):
            print('*',end=" ")
    print()
for i in range(5,-1,-1):
    for j in range(1,i+1):
        print(i,end=" ")
        if(j!=i):
            print("*",end=" ")
    print()

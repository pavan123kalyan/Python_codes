n=int(input("Enter number of rows: "))
for i in range(n,0,-1):
    #space
    for j in range(n-i):
        print(" " ,end=" ") # stay in same line
    for j in range(2*i-1):
        print("*",end=" ")
    print() 

#Approach-2
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*n-(2*i + 1)):
        print("*",end=" ")
    print()


# Enter number of rows: 4
# * * * * * * * 
#   * * * * *
#     * * *
#       *

#Approach-2
n = int(input())
for i in range(n, 0, -1):             # outer loop (rows)
    for j in range(2 * n - 1):        # inner loop (columns)
        if j < n - i or j >= n + i - 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

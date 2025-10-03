n=int(input("Enter number of rows: "))
for i in range(n):
    #space
    for j in range(n-i-1):
        print(" " ,end=" ") # stay in same line
    for j in range(2*i+1):
        print("*",end=" ")
    print()

#     Enter number of rows: 5
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

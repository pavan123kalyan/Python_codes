# What is a Saddle Point?

# An element in a matrix is called a saddle point if:
# -->  it is the minimum in its row
# -->  and maximum in its column
# Simple Intuition (Interview-friendly)

# Think like this:
# Pick an element
# Check:
# Is it the smallest in its row?
# Is it the largest in its column?
# If both true → 🎯 saddle point

#Brute Force(TC: O(n^3))
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flag=False
n=len(matrix)
for i in range(n):
    for j in range(n):
        mat=matrix[i][j]
        if(mat==min(matrix[i])):
            col=[]
            for k in range(n):
                col.append(matrix[k][j])
            if(mat==max(col)):
                
                print("Saddle point is: ",matrix[i][j])
                flag=True
if not flag:
    print("No saddle point")
#Optimal Approach (O(n^2))

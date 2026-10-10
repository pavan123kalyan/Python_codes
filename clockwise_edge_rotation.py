mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = len(mat)
temp = mat[0][0]
# Left column upward
for i in range(n-1):
    mat[i][0] = mat[i+1][0]
# Bottom row left
for i in range(n-1):
    mat[n-1][i] = mat[n-1][i+1]
# Right column downward
for i in range(n-1, 0, -1):
    mat[i][n-1] = mat[i-1][n-1]
# Top row right
for i in range(n-1, 1, -1):
    mat[0][i] = mat[0][i-1]
mat[0][1] = temp
for row in mat:
    print(*row)

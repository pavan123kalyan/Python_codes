mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = len(mat)
temp = mat[0][0]
# Top row left
for i in range(n-1):
    mat[0][i] = mat[0][i+1]
# Right column upwards
for i in range(n-1):
    mat[i][n-1] = mat[i+1][n-1]
# Bottom row right
for i in range(n-1,0,-1):
    mat[n-1][i] = mat[n-1][i-1]
# Left column downward
for i in range(n-1,0,-1):
    mat[i][0] = mat[i-1][0]
mat[1][0] = temp
for row in mat:
    print(*row)

print(0.5==0.5)
p=["yerlin","zRome","Madrisdd"]
print(min(p)) #Madrisdd
print(max(p))#zRome

print(0.1 + 0.5)
print(0.1+0.5==0.6)#True
print(0.1+0.3==0.4)#True
print(0.1+0.2==0.3)#False

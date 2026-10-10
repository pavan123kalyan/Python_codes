#converting matrix into Zig Zag matrix
matr=[[1,2,3],[4,5,6],[7,8,9]]
p=[]
for i in range(len(matr)):
    if(i%2==0):
        p.append(matr[i])
    else:
        p.append(matr[i][::-1])
print(p)

#converting matrix into Zig Zag matrix(array- 1D array form)
mat=[[1,2,3],[4,5,6],[7,8,9]]
l=[]
for i in range(len(mat)):
    if(i%2==0):
        l.extend(mat[i])
    else:
        l.extend(mat[i][::-1])
print(l)
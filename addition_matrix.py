p=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
q=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
res=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
#res=[[]]

for i in range(len(p)):
    for j in range(len(q[0])):
        res[i][j]+=p[i][j]+q[i][j]
for r in res:
    print(r)

# Output:
# [1, 4, 9]
# [16, 25, 36]
# [49, 64, 81]
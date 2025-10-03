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
        for k in range(len(q)):
            res[i][j]+=p[i][k]*q[k][j]
for r in res:
    print(r)

# Output:
# [30, 36, 42]
# [66, 81, 96]
# [102, 126, 150]

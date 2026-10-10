n,m = map(int,input().split())
a = []
for i in range(n):
    row = list(map(int,input().split()))
    a.append(row)
avg = []
for j in range(m):
    s = 0
    for i in range(n):
        s += a[i][j]
    avg.append(s/n)
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > avg[j]:
            cnt += 1
            break
print(cnt)
# 3 3
# 60 70 80
# 50 65 75
# 90 85 88
# 1
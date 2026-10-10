n = 4
A = [10, 20, 50, 40]
B = [50, 20, 10,40]

pos = {}
for i in range(n):
    pos[A[i]] = i
cnt = 0
#print(pos)
for i in range(n):
    if A[i] != B[i]:
        cnt += 1
        idx = pos[B[i]]
        print(idx)
        pos[A[i]] = idx
        pos[A[idx]] = i
        A[i], A[idx] = A[idx], A[i]
print(cnt)

# a,b,h="aa"
# c,d="cd"
# print(a,c)

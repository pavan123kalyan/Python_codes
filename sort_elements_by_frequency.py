arr = [5, 5, 4, 6, 4]
hm = {}
for i in arr:
    hm[i] = hm.get(i, 0) + 1
keys = []
for i in hm:
    keys.append(i)
print(keys)
# manual sort
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        if hm[keys[i]] < hm[keys[j]]:
            keys[i], keys[j] = keys[j], keys[i]
        elif hm[keys[i]] == hm[keys[j]] and keys[i] > keys[j]:
            keys[i], keys[j] = keys[j], keys[i]
# build result 
print(keys)
res = []
for i in keys:
    for j in range(hm[i]):
        res.append(i)

print(res)
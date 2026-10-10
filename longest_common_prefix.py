strs = ["flower","flow","flight"]
strs.sort()
print(strs)
first = strs[0]
last = strs[-1]
print(first)
print(last)
i = 0
while i < len(first) and i < len(last) and first[i] == last[i]:
    i += 1
print(first[:i])


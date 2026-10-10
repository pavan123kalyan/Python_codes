
arr = [ 1, 2, 5, 1, 7, 2, 4, 2 ]

# len of array
n = len(arr)
p=set()
for i in arr:
  if i not in p:
    p.add(i)
p=list(p)
print(p)
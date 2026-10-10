arr = [1,0,1,0,1]
flip = 0
count = 0
for i in arr:
    if (i + flip) % 2 == 0:
        count += 1
        flip = 1 - flip
print(count)
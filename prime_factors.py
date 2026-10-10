n = int(input())
l = []
i = 2
while i <= n:
    if n % i == 0:
        l.append(i)
        n = n // i
    else:
        i += 1
print(l)
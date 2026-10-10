arr = [1, 3, 5, 8, 9]
jumps = 0
end = 0
farthest = 0
for i in range(len(arr)-1):
    farthest = max(farthest, i + arr[i])
    if i == end:
        jumps += 1
        end = farthest
print(jumps)
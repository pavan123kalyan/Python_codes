#selection sort defines the minimum element in each iteration and places it at the beginning
#Best/Worst/Average: O(n²)
arr = [29, 10, 14, 37, 13]
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:   # avoid unnecessary swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
print("Optimized Selection Sort:", arr)
# Output: [10, 13, 14, 29, 37]

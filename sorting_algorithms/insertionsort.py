# Shifts elements instead of multiple swaps.
# Best Case: O(n) (already sorted)
# Worst Case: O(n²)
# Average Case: O(n²)
                
arr = [5, 4, 3, 2, 1]
n = len(arr)
for i in range(n):
    j=i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]  # swap
        j -= 1
print("Sorted array:", arr)

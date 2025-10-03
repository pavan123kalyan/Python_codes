#Repeatedly compares adjacent elements, swapping if they are out of order. After each pass, the largest element “bubbles” to the end.
# ✅ So, the time complexity of your optimized Bubble Sort is:
# Best Case: O(n)
# Worst Case: O(n²)
# Average Case: O(n²)
# Space Complexity: O(1) 
# The optimization with the swap flag allows the algorithm to terminate early if the array becomes sorted before completing all passes.             

arr=[5,3,8,4]
n=len(arr)
for i in range(n):
    swap=0
    for j in range(0,n-i-1): #exclude last i elements
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swap=1
    if(swap==0):
        break
    print("After pass",i+1,":",arr)

print("Bubble sort:",arr)
# Output: [3, 4, 5, 8]
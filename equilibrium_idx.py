#Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
arr = [-7, 1, 5, 2, -4, 3, 0]
#arr=[1,1,1,1]
for i in range(len(arr)):
    # Get left sum
    leftSum = sum(arr[:i])
    # Get right sum
    rightSum = sum(arr[i + 1:])
    # Check the condition
    if leftSum == rightSum:
        print(i)
        break
else:
    print(-1)

#Approach 2
n = len(arr)
pref = [0] * n
suff = [0] * n
pref[0] = arr[0]
suff[n - 1] = arr[n - 1]
# Calculate prefix sum for all indices
for i in range(1, n):
    pref[i] = pref[i - 1] + arr[i]
# Calculating suffix sum for all indices
for i in range(n - 2, -1, -1):
    suff[i] = suff[i + 1] + arr[i]
# Checking if prefix sum 
# is equal to suffix sum
for i in range(n):
    if pref[i] == suff[i]:
        print(i)
        break
else:
    print(-1)
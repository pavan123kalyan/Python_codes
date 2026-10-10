# Given an array of integers and a number k, find the maximum sum of a subarray of size k.
#Sliding window technique, we can maintain a window of size k and keep track of the sum of the elements in the window. We can slide the window from left to right, adding the new element and removing the old element as we go.
a = [1, 2, 3, 4, 5, 6]
k = 3

l = 0
cur_sum = 0
for r in range(len(a)):
    cur_sum += a[r]
    if r - l + 1 == k:
        print(cur_sum,end=" ")
        cur_sum -= a[l]
        l += 1
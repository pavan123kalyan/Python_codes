# Given an array of integers, you can merge two equal integers to get an integer that is one greater.
#You are given an array of integers.

# You can repeatedly:
# Choose any two adjacent elements
# If they are equal → remove both
# Insert one element with value +1 in their place
# Array is circular (first and last are also adjacent)

# Your task:
# 👉 Perform operations any number of times
# 👉 Find the maximum possible element in the final array.

def max_element_after_merges(arr):
    hm = {}
    # Step 1: Count frequency
    for i in arr:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1 
    # Step 2: Process values in sorted order
    keys = sorted(hm.keys())
    i = 0
    while i < len(keys):
        val = keys[i]
        if hm[val] >= 2:
            carry = hm[val] // 2
            hm[val] %= 2
            next_val = val + 1
            if next_val in hm:
                hm[next_val] += carry
            else:
                hm[next_val] = carry
                keys.append(next_val)   # new key added
        i += 1
    return max(hm.keys())
print(max_element_after_merges([5,3,3,3,4])) # Output: 6

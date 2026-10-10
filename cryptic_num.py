# Question 1: Cryptic Numbers (Easy Category)
# 🧠 Problem Summary
# You are given two integers:
# start
# end
# You must print numbers in the range [start, end] that satisfy all conditions:
# 1️⃣ Number is divisible by 7
# 2️⃣ Number is not divisible by 5
# 3️⃣ Number is not a palindrome
# 4️⃣ Number has no repeated digits

# Output the valid numbers in ascending order separated by space.
s,e = map(int,input().split())
for i in range(s,e+1):
    if i % 7 != 0:
        continue
    if i % 5 == 0:
        continue
    x = str(i)
    if x == x[::-1]:
        continue
    if len(set(x)) != len(x):
        continue
    print(i,end=" ")
# Given a string s, find the length of the longest palindromic subsequence in s. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
s = input().strip()
t = s[::-1]
n = len(s)
#dp = [[0]*(n+1) for _ in range(n+1)]
dp = []
for _ in range(n+1):
    dp.append([0]*(n+1))
print(dp)
for i in range(1, n+1):
    for j in range(1, n+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            #print(dp)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp)
print(dp[n][n])
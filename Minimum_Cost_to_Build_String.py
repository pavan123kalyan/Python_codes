s2 = "abcbcaa"
A = 2
B = 3
n = len(s2)
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    # Append single character
    dp[i] = dp[i-1] + A
    
    # Try copying substring
    for j in range(i):
        sub = s2[j:i]
        if sub in s2[:j]:
            dp[i] = min(dp[i], dp[j] + B)

print(dp[n])

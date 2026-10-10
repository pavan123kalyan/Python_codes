#Approach 1
n = 5
sq = n*n
d = len(str(n))
if sq % (10**d) == n:
    print("automorphic")
else:
    print("No")

#approach 2
n=25
p=str(n*n)
if p.endswith(str(n)):
    print("automorphic")
else:
    print("No")

#approach 3
n = 25
sq = str(n*n)
if sq[-len(str(n)):] == str(n):
    print("automorphic")
else:
    print("No")
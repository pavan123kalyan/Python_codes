#Approach - 1
from math import log10
n=784
c=log10(n)+1
print(int(c)) #3

#Approach - 2
class Solution:
    def countDigit(self, n):
        c=0
        while(n>0):
            lastdigit=n%10
            c+=1
            n=n//10
        print(c)
# Create object of Solution
obj = Solution()
# Call the method
obj.countDigit(784)   # Output: 3
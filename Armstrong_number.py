# An Armstrong number is a number that equals the sum of its own digits, each raised to the power of the total number of digits. 
# For example, 153 is an Armstrong number because it has three digits, 
# and 1³ + 5³ + 3³ = 1 + 125 + 27 = 153. Other examples include 370, 371, and 1634


class Solution:
    def isArmstrong(self,n):
        dup=n
        sum1=0
        p=len(str(n))
        while(n>0):
            ld=n%10
            sum1+=(ld**p)
            n=n//10
        if(sum1==dup):  
            print(f"{dup}  is a Armstrong number")
        else:
            print(f"{dup}  is not a Armstrong number")
obj=Solution()
obj.isArmstrong(153)#153=1^3 + 5^3 + 3^3
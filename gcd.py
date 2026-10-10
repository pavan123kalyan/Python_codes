#Approach- 1(BruteForce) ,Works fine but is slow if numbers are large.
#TC: 
n1,n2=20,40
for i in range(1,min(n1,n2)+1):
    if(n1%i==0 and n2%i==0):
        gcd=i
        print(i)  # prints all common divisors
print("Gcd is",gcd)

#✅ 2. Euclidean Algorithm (efficient)
#gcd(a,b)=gcd(a-b,b)  -->eg., 
#gcd(10,2)=gcd(8,2)=gcd(6,2)=gcd(4,2)=gcd(2,2)=gcd(0,2)

#Subtraction method:
#20,40
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
print("By using Subtraction,  GCD =", gcd(20, 40))

#or we can easily do without more steps, 
#gcd(a,b)=gcd(a%b,b)
#gcd(10,2)=gcd(10%2,2)=gcd(0,2)  in single step we came,whereas in above we have many steps
#Modulus method (much faster):
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("By using individual,  GCD =", gcd(20, 40))
#or
def gcd(a, b):
    while(a>0 and b>0):
        if(a>b):
            a=a%b
        else:
            b=b%a
    if(a==0):
        return b
    return a

print("by Using Modulo ,GCD =", gcd(20, 40))

#✅ 3. Using Python’s built-in function
import math

print("By using inbuilt method, GCD =", math.gcd(20, 40))  # Output: 20
#Brute force → good for understanding.
#Euclidean algorithm (a % b) → efficient for large numbers.
#math.gcd() → easiest in real projects.

import math
print(math.gcd(0, 5))  # 5
import math
print(math.gcd(5,0))  # 5



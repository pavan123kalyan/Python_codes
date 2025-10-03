def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

n1, n2 = 20, 40
print("GCD =", gcd(n1, n2))
print("LCM =", lcm(n1, n2))

#✅ Example 2: Using Python’s built-in math module
import math

n1, n2 = 20, 40
print("GCD =", math.gcd(n1, n2))
print("LCM =", math.lcm(n1, n2))
#If you’re on an older version, use the formula (a*b)//gcd(a,b).

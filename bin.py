def to_binary(n):
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res
print(to_binary(12))

print(bin(12)[2:]) #The built-in bin() function in Python converts an integer to its binary representation as a string. The output will be '0b1100', where '0b' is a prefix indicating that the number is in binary format.

#Binary to Decimal
p="1010"
n=len(p)
s=0
for i in range(n):
  if(p[i]=='1'):
  	s+=2**(n-i-1)
print(s)
  
#✅ Method 1: Using string reversal
n = 121
if str(n) == str(n)[::-1]:
    print(f"{n} is a Palindrome number")
else:
    print(f"{n} is not a Palindrome number")

#✅ Method 2: Using math (without converting to string)
n = 12321
temp = n
rev = 0

while n > 0:
    ld = n % 10          # last digit
    rev = rev * 10 + ld  # build reverse number
    n = n // 10

if temp == rev:
    print(f"{temp} is a Palindrome number")
else:
    print(f"{temp} is not a Palindrome number")

n = 12321
temp = n
rev = 0
p=[]
while n > 0:
    ld = n % 10          # last digit
    p.append(ld)  # build reverse number
    n = n // 10
rev = int(''.join(map(str, p)))

if temp == rev:
    print(f"{temp} is a Palindrome number")
else:
    print(f"{temp} is not a Palindrome number")
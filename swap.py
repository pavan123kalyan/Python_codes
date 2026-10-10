#Swapping without using third variable using arithmetic operations
a=12
b=10
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

#Swapping without using third variable using XOR operator
a=20
b=30
a=a^b
b=a^b
a=a^b   
print("After swapping: a =", a, "b =", b)

# x=25
# b=x++ + ++x - x++
# Given x = 25
# Evaluation (Java logic):
# Step by step:
# x++ → returns 25, x becomes 26
# ++x → x becomes 27, returns 27
# x++ → returns 27, x becomes 28
# Expression:
# = 25 + 27 - 27
# = 25

# Final x = 25
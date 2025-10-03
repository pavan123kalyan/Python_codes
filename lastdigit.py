#extraction of digits in reverse order
#It prints last digit of number which gives reminder by 10
n=7789
while(n>0):
    lastdigit=n%10
    n=n//10
    print(lastdigit)   
# output: 9
# 8
# 7
# 7
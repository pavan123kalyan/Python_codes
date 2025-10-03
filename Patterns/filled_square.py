for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        for j in range(n):
            print("*",end="") # stay in same line
        print()   # move to next line after each row

# C:\Users\paidi\Music\Python_codes\Patterns>python filled_square.py
# 2
# 3
# ***
# ***
# ***
# 5
# *****
# *****
# *****
# *****
# *****
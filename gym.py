n = int(input())
tot = 0
if n <= 0 or n % 3 != 0:
    print("Invalid input")
else:
    while n >= 12:
        tot += 15000
        n -= 12
    while n >= 9:
        tot += 12000
        n -= 9
    while n >= 6:
        tot += 9000
        n -= 6
    while n >= 3:
        tot += 5000
        n -= 3
    if n == 1:
        tot += 2000
    print(tot)
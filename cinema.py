'''Find the count, sum and average of all odd numbers in an ticket price array.
Conditions:
If n > 30, print "error".
If any array element is greater than 10000, print "error".
Otherwise:
Print the count of all odd numbers.
Print the sum of all odd numbers.
Print the average of odd numbers rounded to 2 decimal places.'''

n = int(input())
if n > 30:
    print("error")
else:
    a = list(map(int, input().split()))
    c = 0
    sum1 = 0
    flag = True
    for i in range(n):
        if a[i] > 10000:
            flag = False
        if flag and a[i] % 2 == 1:
            sum1 += a[i]
            c += 1
    if flag:
        print(c)
        print(sum1)
        print("%.2f" % (sum1 / c))
    else:
        print("error")
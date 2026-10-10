# Starting date
day = 23
month = 2
year = 2026
n = 439
# Days in months (normal year first)
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while n > 0:
    # Check leap year
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        months[1] = 29
    else:
        months[1] = 28
    # Remaining days in current month
    remaining = months[month - 1] - day
    if n <= remaining:
        day += n
        n = 0
    else:
        n -= (remaining + 1)
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
#print("Final Date:", day,month,year)
#print(str(day) + "-" + str(month) + "-" + str(year))
#print(day, "-", month, "-", year)

print(f"{day:02d}-{month:02d}-{year}")
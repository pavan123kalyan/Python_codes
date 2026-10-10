num = 3749
hm={1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',100: 'C', 90: 'XC', 50: 'L', 40: 'XL',10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
res=""
for val in hm:
    while(num>=val):
        res+=hm[val]
        num-=val
print(res)
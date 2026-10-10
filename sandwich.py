'''🧩 Problem: Closest Sandwich Cost
You are given two arrays:
bread[]: represents the cost of different types of bread.
filling[]: represents the cost of different fillings.

You want to make a sandwich by:
Choosing exactly one bread.
For each filling, you can choose:
0 units, 1 unit, or 2 units of that filling.
Given a target cost target, your goal is to compute the total cost of the sandwich such that:
The total cost is as close as possible to the target.
If there are multiple costs equally close to the target, return the smallest such cost.'''

bread = [5,7,8,6,2]
filling = [5,30,5,40,10]
target = 20
s = {0}
for x in filling:
    temp = set()
    for v in s:
        temp.add(v)
        temp.add(v + x)
        temp.add(v + 2 * x)
    s = temp
print(s) #Output: {0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} The set s contains all possible sums of the fillings (0 means no filling, 2 means one unit of the first filling, 3 means one unit of the second filling, and so on). The total number of combinations is 3^n where n is the number of fillings (in this case, n=2), so we have 3^2 = 9 combinations plus the case of no filling (0), resulting in a total of 10 unique sums.

res = float('inf')
for b in bread:
    for v in s:
        cur = b + v
        if abs(target-cur) < abs(target-res):
            res = cur
            #print(res)
        elif abs(target - cur) == abs(target - res):
            res = min(res, cur)
print(res)
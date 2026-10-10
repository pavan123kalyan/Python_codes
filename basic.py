#Area of Circle upto 5 decimal places
r = 5
p = 3.14 * r * r
print("{:.5f}".format(p))

n=[1,2,3,4,5]
for i in n:
    if i==3:
        n.remove(i)
print(n)
#Output: [1, 2, 4, 5]
#The above code removes the element 3 from the list n. However, it is generally not recommended to modify a list while iterating over it, as it can lead to unexpected behavior. In this case, the loop will skip the next element after removing 3, which is why 4 is not removed from the list.
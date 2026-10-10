#Lambda funtion is a small anonymous function that can take any number of arguments, but can only have one expression. It is defined using the lambda keyword followed by the arguments, a colon, and the expression. For example:  
input="hashjjiirrhh"
hm={}
for i in input:
    hm[i]=hm.get(i,0)+1
res=sorted(hm.items(), key=lambda x: x[1], reverse=True)
print(res)
print(hm) #Output: {'h': 4, 'a': 1, 's': 1, 'j': 2, 'i': 2, 'r': 2}
print(res[1][0])

#Lamda function: A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is defined using the lambda keyword followed by the arguments, a colon, and the expression. For example:
add = lambda a, b: a + b
print(add(2, 3))

#res=sorted(hm.items(), key=lambda x: x[1], reverse=True)

# 1.map() --> Used to apply some operation on every element.
arr = [1, 2, 3, 4]
res = list(map(lambda x: x * 2, arr))
print(res) #Output: [2, 4, 6, 8] The map function applies the lambda function to each element of the arr list, multiplying each element by 2 and returning a new list with the results.

#2. filter() --> Used to filter out elements from a list based on some condition.
arr = [1, 2, 3, 4, 5, 6]
res = list(filter(lambda x: x % 2 == 0, arr))
print(res) #Output: [2, 4, 6] The filter function applies the lambda function to each element of the arr list and returns a new list containing only the elements that satisfy the condition (in this case, being even).

#3. sorted() --> Used to sort a list based on some key or condition.
arr = [(1, 5), (2, 3), (3, 8)]
res = sorted(arr, key=lambda x: x[1])
print(res) #Output: [(2, 3), (1, 5), (3, 8)] The sorted function sorts the arr list based on the second element of each tuple (x[1]) in ascending order. If you want to sort in descending order, you can add the reverse=True parameter to the sorted function.

#4. reduce() --> Used to apply a rolling computation to sequential pairs of values in a list. It is part of the functools module, so you need to import it before using it.
from functools import reduce
arr = [1, 2, 3, 4]
res = reduce(lambda x, y: x + y, arr)
print(res) #Output: 10 The reduce function applies the lambda function cumulatively to the items of the arr list, from left to right, so it calculates (((1 + 2) + 3) + 4) and returns the final result, which is 10.
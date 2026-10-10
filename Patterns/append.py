
print ('Hello World')
p=[1,2]
q=[3,4]
p.extend(q)
print(p)
print(len(p))

e=[1,2,3]
e.append("pavan")
e.extend("pavan")
print(e)
a=-7 #output: 6
#a=5 #output: -6
print(~a)

print('a'and'b') #b
print('a'and 'a') #a
print('a'or 'b') #a

#Python generators are special functions that allow you to create iterators in a memory-efficient way. Instead of returning a complete list and ending, a generator "yields" values one at a time, pausing its execution and maintaining its internal state until the next value is requested.
#Generators - Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example of a generator function that counts up to a specified number is shown below:

#generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
obj=count_up_to(10)
print(next(obj)) #output: 1
print(next(obj)) #output: 2

#Generator expressions
squares = (x**2 for x in range(5,10)) #Generator expression - A generator expression is a compact generator notation in Python. It is similar to a list comprehension but uses parentheses instead of square brackets. Generator expressions are more memory efficient than list comprehensions because they generate items one at a time and do not store the entire list in memory. The syntax for a generator expression is: (expression for item in iterable if condition). For example, to create a generator that produces the squares of numbers from 5 to 9, you can use the following code:
print(next(squares)) #output: 25

squares = [x**2 for x in range(5,10)]
print(squares)#output: [25, 36, 49, 64, 81]

print(['a','b'] or 'a')


#Removing adjacent duplicates from a string using a stack
s='abbaca'
stack=[]
for i in s:
    if( stack and stack[-1]==i):
        stack.pop()
    else:
        stack.append(i)
print(''.join(stack)) #output: "ca"

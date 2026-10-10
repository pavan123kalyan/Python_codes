#Generators in python are a powerful tool for creating iterators that can be used to iterate over large datasets without consuming a lot of memory. They allow you to generate values on the fly, which can be more efficient than creating a complete list in memory. Here are some examples of how to use generators in Python:       
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib_gen = fibonacci(10)
for num in fib_gen:
    print(num)

#Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets. For example, to create a generator that produces the squares of numbers from 0 to 9, you can use the following code:
squares = (x**2 for x in range(10))
for square in squares:
    print(square)

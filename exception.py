#Exception Handling
# Exception handling is a way to handle runtime errors(unexpected errors) so that the program doesn't crash and we can take proper action instead.
#Error Happened --> I know how to handle it.
a=10
b=0
try:
    print(a/b)
except:
    print("Cannot divide by zero")

#Multiple Inheritance 
#Python allows multiple Inheritance,it uses a rule called MRO(Method Resolution Order)
class B:
    pass
class C:
    pass
class A(B,C):
    pass
# food="pizza"
# food.replace("z","l")
# print(food) #pizza -->Strings are immutable in Python, so the replace method does not change the original string. It returns a new string with the replacements. To see the change, you need to assign the result back to a variable (either the same variable or a new one).

# food="pizza"
# new_food=food.replace("z","l")
# print(new_food)

# p=(1,2,3)
# print(hash(p)) #Tuples are immutable and hashable, so you can use them as keys in a dictionary or store them in a set. The hash value of a tuple is based on the hash values of its elements.
# # p=[1,[2,3]]
# # print(hash(p)) #Lists are mutable and unhashable, so you cannot use them as keys in a dictionary or store them in a set. Attempting to hash a list will raise a TypeError.

# l=["apple","bana"]
# for i in l:
#     l.append("guava")
# print(l)

cars=["Porsche","BMW","Audi"]
trending=[]
for c in cars:
    if c=="BMW" or "Audi": #Here, the condition is always true because "Audi" is a non-empty string, which is considered truthy in Python. To check if c is either "BMW" or "Audi", you should use the following condition:
        
        trending.append(c)
print(trending)

x=[7,7]
y=[7,7]
if x is y:#if x==y: #Output: Equal. The equality operator (==) checks for value equality, and since x and y have the same contents (the same list of integers), they are considered equal. The identity operator (is) checks for object identity, and since x and y are different objects in memory, it would return False. Therefore, using x == y is the correct way to check for value equality in this case.
    print("Equal")
else:
    print("Not Equal") #Output: Equal. In Python, the equality operator (==) checks for value equality, not identity. Since x and y have the same contents (the same list of integers), they are considered equal, even though they are different objects in memory.


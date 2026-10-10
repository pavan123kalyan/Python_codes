#It returns the index of first occurrence of the substring in the given string. If the substring is not found, it returns -1.
txt = "geopeksforgeeks"
pat = "eks"
idx = txt.find(pat)
print(idx)

#Approach 2
txt = "geopeksforgeeks"
pat = "eks"
idx = txt.index(pat)
print(idx)



# p=float('inf')
# q=3
# print(max(p,q))



x = 10
def func():
    print(x)
    #x = 5
func() #output: 10

x = 10
def func():
    print(x)
    x = 5
func() #output: unbound local error
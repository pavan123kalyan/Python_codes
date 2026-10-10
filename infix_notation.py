#input:*+ABC
#output:((A+B)*C)
#prefix notation to infix notation

s = input().strip()
stack = []
operators = set(['+', '-', '*', '/', '^'])
for i in range(len(s) - 1, -1, -1):
    ch = s[i]
    if ch not in operators:
        stack.append(ch)
    else:
        a = stack.pop()
        b = stack.pop()
        res = "(" + a + ch + b + ")"
        stack.append(res)
#print(stack) ,we get list format with one element which is the final result
#print(stack[0])
print(stack[-1]) #removing list format and getting the string format of the result
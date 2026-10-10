s='1abc23'
temp="0"
s1=0
for i in s:
  if i.isdigit():
    temp+=i
  else:
    s1+=int(temp)
    temp="0"
print(s1+int(temp))
#output: 24



#Approach 2
s='1abc23'  
s1=0
temp=""
for i in s: 
    if i.isdigit():
        temp+=i
    else:
        s1+=int(temp) if temp else 0
        temp=""
s1+=int(temp) if temp else 0
print(s1)

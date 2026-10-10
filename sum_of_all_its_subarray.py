# #Bruteforce --> O(n^3)
# l=[1,2,3,4,5,6]
# n=len(l)
# p=0
# for i in range(n):
#     for j in range(i,n):
#         s=l[i:j+1]
#         p+=sum(s)
#         print(s)
# print(p)
        
# #Optimized --> O(n^2)
# l=[1,2,3,4,5,6]
# n=len(l)
# s=0
# for i in range(n):
#     p=0
#     for j in range(i,n):
#         p+=l[j]
#         s+=p
#         print(s)
# #Most optimized --> O(n)
# l=[1,2,3,4,5,6]
# n=len(l)
# s=0
# for i in range(n):
#     s+=l[i]*(n-i)*(i+1)
#     print(s)

p=[3,4,5]
pre=[1]*len(p)


        
        
        
        
        

         
        
        
        
        
        
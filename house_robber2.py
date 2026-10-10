#It is a well-known problem called "House Robber II". The idea is to determine the maximum amount of money you can rob from a list of houses arranged in a circle, where adjacent houses cannot be robbed on the same night. This means that the first and last houses are also adjacent.
nums = [2,3,2]
if(len(nums)==1):
    print(nums[0])
if(len(nums)==2):
    print(max(nums))
c1,c2=0,0
for i in range(len(nums)-1):
    mini_1=max(c1,c2+nums[i])
    c2=c1
    c1=mini_1
c1 = 0  
c2 = 0
for j in range(1,len(nums)):
    mini_2=max(c1,c2+nums[j])
    c2=c1
    c1=mini_2
print(max(mini_1,mini_2))



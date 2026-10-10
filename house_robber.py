#It is a well-known problem called "House Robber". The idea is to determine the maximum amount of money you can rob from a list of houses, where adjacent houses cannot be robbed on the same night.
nums = [2,1,1,2]
c1,c2=0,0
for i in range(len(nums)):
    temp=max(c1,c2+nums[i])
    c2=c1 
    c1=temp
print(temp)
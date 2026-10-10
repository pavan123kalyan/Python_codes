import heapq
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
p=[]
for i in range(len(intervals)):
    if(p and p[0]<=intervals[i][0]):
        heapq.heappop(p)
    heapq.heappush(p,intervals[i][1])
print(len(p))
x=9
lambda x:x*x
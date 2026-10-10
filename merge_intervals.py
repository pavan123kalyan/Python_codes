intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
#print(intervals)
p=[intervals[0]]
for i in range(1,len(intervals)):
    if(intervals[i][0]<=p[-1][1]):#overlap
        p[-1][1]=max(intervals[i][1],p[-1][1])
    else:
        p.append(intervals[i])
print(p)

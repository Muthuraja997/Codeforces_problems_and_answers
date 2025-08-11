from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        d=[]
        intervals.sort(key=lambda x:x[0])
        for i in intervals:
            if not d or i[0]>d[-1][-1]:
                d.append(i)
            else:
                d[-1][0]=min(d[-1][0],i[0])
                d[-1][-1]=max(d[-1][-1],i[-1])
        return d
    

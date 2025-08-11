from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n=len(intervals)
        pre=0
        count=1
        for i in range(1,n):
            if intervals[i][0]>=intervals[pre][1]:
                count+=1
                pre=i
        return n-count
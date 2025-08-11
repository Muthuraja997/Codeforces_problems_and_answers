from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m=0
        n=len(nums)
        o=0
        j=0
        for i in range(n):
            if nums[i]==0:
                o+=1
            while o>1:
                if nums[j]==0:
                    o-=1
                j+=1
            m=max(m,i-j)
        return m
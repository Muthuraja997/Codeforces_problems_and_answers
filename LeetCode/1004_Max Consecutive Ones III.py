from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       n=len(nums)
       j=0
       z=0
       m=0
       for i in range(n):
            if nums[i]==0:
                z+=1
            while z>k:
                if nums[j]==0:
                    z-=1
                j+=1
            m=max(m,i-j+1)
       return m
                
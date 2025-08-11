from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1 or len(nums)==0:
            return 0
        nums.sort()
        n=len(nums)
        m=float('inf')
        for i in range(n-k+1):
            dif=nums[i+k-1]-nums[i]
            if dif<m:
                m=dif
        return m
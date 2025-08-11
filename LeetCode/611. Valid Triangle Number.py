from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=0
        for l in range(n-2):
            i,j=l+1,l+2
            while j<n:
                if (nums[i]+nums[l])>nums[j]:
                    count+=(j-i)
                    j+=1
                else:
                    i+=1
                    if i==j:
                        j+=1
        return count
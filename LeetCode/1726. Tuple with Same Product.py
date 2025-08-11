from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                v1=nums[i]*nums[j]
                if v1 not in d.keys():
                    d[v1]=[nums[i],nums[j]]
                else:
                    d[v1].append(nums[i])
                    d[v1].append(nums[j])

        ans=0
        for i in d:
            if len(d[i])>2:
                ans+=(len(d[i])*(len(d[i])-2))
        return ans
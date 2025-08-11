from typing import List
import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            ele=heapq.heappop(nums)
            heapq.heappush(nums,ele+1)
        p=1
        for i in nums:
            p=(p*i)%(10**9+7)
        return p
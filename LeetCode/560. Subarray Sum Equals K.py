from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}  
        sm = 0  
        count = 0  

        for num in nums:
            sm += num  
            if (sm - k) in prefix_sums:
                count += prefix_sums[sm - k]  
            prefix_sums[sm] = prefix_sums.get(sm, 0) + 1  

        return count

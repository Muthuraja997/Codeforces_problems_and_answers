from typing import List
import collections
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s=set()
        c=collections.defaultdict(int)
        tot=0
        l=0
        res=0
        for i in range(len(fruits)):
            c[fruits[i]]+=1
            tot+=1
            while len(c) > 2:
                c[fruits[l]]-=1
                tot-=1
                if not c[fruits[l]]:
                    c.pop(fruits[l])
                l+=1
            res=max(res,tot)
        return res
                


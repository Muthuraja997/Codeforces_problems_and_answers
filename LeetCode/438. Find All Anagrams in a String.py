from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=list(p)
        p.sort()
        i=0
        l=[]
        k=len(p)
        while (i+k)<=len(s):
            nl=list(s[i:i+k])
            nl.sort()
            if nl==p:
                l.append(i)
            i+=1
        return l
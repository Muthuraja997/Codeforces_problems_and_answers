import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=collections.Counter()
        ll=0
        ml=0
        for i in range(len(s)):
            d[s[i]]+=1
            ll=max(ll,d[s[i]])
            if ml-ll>=k:
                d[s[i-ml]]-=1
            else:
                ml+=1
        return ml
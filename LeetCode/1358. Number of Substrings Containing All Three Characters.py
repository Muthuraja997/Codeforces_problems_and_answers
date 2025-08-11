class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        d={}
        res=0
        l=0
        for i in 'abc':
            d[i]=0
        for r in range(len(s)):
            d[s[r]]+=1
            while d['a']!=0 and d['b']!=0 and d['c']:
                d[s[l]]-=1
                l+=1
                res+=(n-r)
        return res 
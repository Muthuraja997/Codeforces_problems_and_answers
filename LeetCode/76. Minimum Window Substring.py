from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        st=defaultdict(int)
        tt=defaultdict(int)
        for i in t:
            tt[i]+=1
        need=len(tt)
        have=0
        l=0
        m=float('inf')
        inx=[0,0]
        for r in range(len(s)):
            c=s[r]
            st[c]+=1
            if c in tt and st[c]==tt[c]:
                have+=1
            while have==need:
                c=s[l]
                if c in st:
                    st[c]-=1
                    if st[c]<tt[c]:
                        have-=1
                if m>=r-l+1:
                    m=r-l+1
                    inx=[l,r+1]
                l+=1
        return s[inx[0]:inx[1]]

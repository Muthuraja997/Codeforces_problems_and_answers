class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        l=[]
        for r in range(len(s)):
            while s[r] in l:
                l.pop(0)
            l.append(s[r])
            m=max(m,len(l))
        return m     
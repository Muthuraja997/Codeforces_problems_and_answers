from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        v=0
        for i in range(m+n):
            if nums1[i]==0 and v<len(nums2):
                nums1[i]=nums2[v]
                v+=1
        for i in range(len(nums1)):
            mi=i
            for j in range(i+1,len(nums1)):
                if nums1[j]<nums1[mi]:
                    mi=j
            nums1[i],nums1[mi]=nums1[mi],nums1[i]
        return nums1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1=Counter(nums1)
        d2=Counter(nums2)
        a=[]
        b=[]
        for i in d1:
            if i not in d2:
                a.append(i)
        for i in d2:
            if i not in d1:
                b.append(i)
        return [a,b]
        
                
        
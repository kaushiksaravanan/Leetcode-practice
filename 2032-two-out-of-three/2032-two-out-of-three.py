class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        k=set()
        for i in nums1:
            if nums1.count(i)>0 and nums2.count(i)>0:
                k.add(i)
            if nums1.count(i)>0 and nums3.count(i)>0:
                k.add(i)
            if nums2.count(i)>0 and nums3.count(i)>0:
                k.add(i)
        for i in nums2:
            if nums2.count(i)>0 and nums1.count(i)>0:
                k.add(i)
            if nums2.count(i)>0 and nums3.count(i)>0:
                k.add(i)
            if nums1.count(i)>0 and nums3.count(i)>0:
                k.add(i)
        for i in nums3:
            if nums1.count(i)>0 and nums3.count(i)>0:
                k.add(i)
            if nums2.count(i)>0 and nums3.count(i)>0:
                k.add(i)
            if nums2.count(i)>0 and nums1.count(i)>0:
                k.add(i)
        # print(set(k))
        return list(k)
        
            
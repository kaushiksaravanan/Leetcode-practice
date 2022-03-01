class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ri=[]
        for i in nums1:
            k=0
            for j in nums2:
                if i==j:
                    break
                k+=1
            print(k)
            for r in range(k,len(nums2)):
                if nums2[k]<nums2[r]:
                    ri.append(nums2[r])
                    break
                if r==len(nums2)-1:
                    ri.append(-1)
            if k==len(nums2):
                ri.append(-1)
        return ri
            
                    
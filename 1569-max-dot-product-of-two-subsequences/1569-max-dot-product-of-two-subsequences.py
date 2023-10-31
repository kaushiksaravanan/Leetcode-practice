class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1=len(nums1)
        n2=len(nums2)

        @cache
        def rec(i=0,j=0,c=False):
            if i==n1 or j==n2:
                return 0 if c>=1 else -999999999999
            return max(rec(i+1,j,c),rec(i,j+1,c),rec(i+1,j+1,True)+(nums1[i]*nums2[j]))

        return rec()


        
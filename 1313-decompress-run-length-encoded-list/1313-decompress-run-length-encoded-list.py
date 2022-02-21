class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                k.append(nums[i+1])
        return k
        
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m=[i for i in range(1,len(nums)+1)]
        return list(set(m).difference(set(nums)))
        # for i in range(len(nums)):
            
        
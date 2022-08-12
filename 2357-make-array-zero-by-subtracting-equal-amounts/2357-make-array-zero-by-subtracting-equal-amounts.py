class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        for i in range(nums.count(0)):
            nums.remove(0)
        return len(set(nums))
        
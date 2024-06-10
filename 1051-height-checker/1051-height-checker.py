class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 if i!=j else 0 for i,j in zip(sorted(heights),heights)])
        # return count([1 for i,j in sorted(heights),heights if i!=j])
        
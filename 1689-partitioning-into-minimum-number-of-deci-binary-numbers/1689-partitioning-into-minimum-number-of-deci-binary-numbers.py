class Solution:
    def minPartitions(self, n: str) -> int:
       return max(int(i) for i in list(str(n)))
        
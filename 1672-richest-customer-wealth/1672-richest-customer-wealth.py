class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        k=0
        for i in accounts:
            y=sum(i)
            if y>k:
                k=y
        return k
        
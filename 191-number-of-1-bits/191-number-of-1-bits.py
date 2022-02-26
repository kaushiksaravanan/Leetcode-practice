class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(int(n)).replace("0b", "").count("1")
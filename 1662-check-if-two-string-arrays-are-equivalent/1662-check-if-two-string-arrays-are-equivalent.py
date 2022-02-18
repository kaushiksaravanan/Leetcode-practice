class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        k=""
        for i in word1:
            k+=i
        l=""
        for i in word2:
            l+=i
        return k==l
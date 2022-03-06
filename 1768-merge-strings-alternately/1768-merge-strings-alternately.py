class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        k=1
        for i in range(0,len(word2)):
            word1.insert(i+k,word2[i])
            k+=1
        k=len(word2)-len(word1)
        for i in range(k,0,-1):
            word1.append(word2[i])
        return "".join(word1)
        
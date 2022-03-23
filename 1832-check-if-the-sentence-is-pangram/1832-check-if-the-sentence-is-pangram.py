class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alp='abcdefghijklmnopqrstuvwxyz'
        sen=list(set(list(sentence)))
        sen.sort()
        sen="".join(sen)
        return alp==sen
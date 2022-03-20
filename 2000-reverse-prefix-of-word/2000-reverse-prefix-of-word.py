class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        fin=word
        try:
            k=word.index(ch)
            fin=word[:k+1][::-1]+word[k+1:]
        except:
            pass
        return fin
        
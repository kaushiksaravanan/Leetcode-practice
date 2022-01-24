class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return(word.upper()==word or word.lower()==word or (word[0].upper()+word[1:].lower())==word)
        
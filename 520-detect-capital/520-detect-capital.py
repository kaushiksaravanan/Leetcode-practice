class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper()==word or word.lower()==word or (word[0].upper()+word[1:].lower())==word:
            return True
        return False
        
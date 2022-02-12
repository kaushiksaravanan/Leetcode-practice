class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        for i in letters:
            if i>target:
                return i
        for i in letters:
            if i<target:
                return i
        return "null"
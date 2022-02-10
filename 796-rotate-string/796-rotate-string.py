class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        k=len(s)
        for i in range(k):
            r=s[-i:]+s[:-i]
            if r==goal:
                return True
        return False
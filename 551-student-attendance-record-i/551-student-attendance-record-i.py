class Solution:
    def checkRecord(self, s: str) -> bool:
        print(s.count('LLL'),s.count('A')>=2)
        return s.count('LLL')==0 and s.count('A')<2
        
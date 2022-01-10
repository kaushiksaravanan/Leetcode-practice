class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.replace(" ","")
        for i in s:
            if i.isdigit():
                continue
            if not(i.isalpha()):
                t=t.replace(i,"")
        t=t.lower()
        print(t)
        return t==t[::-1]
        
        
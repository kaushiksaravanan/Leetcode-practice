class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        k=text.split()
        for i in k:
            temp=0
            le=0
            for letters in brokenLetters:
                if letters not in i:
                    temp+=1
                # if letters in i:
                #     break
                le+=1
            print(temp,le)
            if le==temp:
                c+=1
        return c
                
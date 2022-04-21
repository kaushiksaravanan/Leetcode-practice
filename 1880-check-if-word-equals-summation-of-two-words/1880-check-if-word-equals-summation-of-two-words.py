class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alp='abcdefghijklmnopqrstuvwxyz'
        num1=''
        for i in firstWord:
                num1+=str(alp.index(i))
        num2=''
        for i in secondWord:
                num2+=str(alp.index(i))
        num3=''
        for i in targetWord:
                num3+=str(alp.index(i))
        return int(num1)+int(num2)==int(num3)
        
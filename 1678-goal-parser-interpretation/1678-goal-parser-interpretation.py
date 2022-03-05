class Solution:
    def interpret(self, s: str) -> str:
        k=""
        for i in range(len(s)-1):
            if s[i]=='(' and s[i+1]==')':
                k+='o'
            if s[i]=='(' and s[i+1]=='a':
                k+='al'
            if s[i]=='G':
                k+=s[i]
        if s[-1]=='G':
            k+='G'
        return k
                
            
        return s.replace("(al)","al").replace("()","o")
        
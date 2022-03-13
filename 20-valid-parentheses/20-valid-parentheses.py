class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        k=len(s)
        x=0
        if k==1:
            return False
        for i in s:
            try:
                if i=='(' or i=='{' or i=='[':
                    stack.append(i)
                if i==')':
                    if(len(i)==0 or stack.pop()!='('):
                        return False
                if i=='}':
                    if(len(i)==0 or stack.pop()!='{'):
                        return False
                if i==']':
                    if(len(i)==0 or stack.pop()!='['):
                        return False
                x+=1
            except:
                return False
            if x==k and len(stack)==0:
                return True
                
                    
        
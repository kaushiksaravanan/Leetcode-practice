class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        x=[]
        # fl=[-2]*len(s)
        def f(index,flag,x):
            if index>=len(s):
                l=0
                ss=''
                for i in flag:
                    if i==1:
                        ss+=s[l].lower()
                    elif i==0:
                        ss+=s[l].upper()
                    elif i==-1:
                        ss+=s[l]
                    l+=1
                x.append(ss[:])
                return
            if not s[index].isdigit():
                flag[index]=1
                f(index+1,flag,x)
                flag[index]=0
                f(index+1,flag,x)
            else:
                flag[index]=-1
                f(index+1,flag,x)
        f(0,[-2]*len(s),x)
        return x
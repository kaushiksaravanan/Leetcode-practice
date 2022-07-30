class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        x=[]
        flag=[-2]*len(s)
        def f(index):
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
                f(index+1)
                flag[index]=0
                f(index+1)
            else:
                flag[index]=-1
                f(index+1)
        f(0)
        return x
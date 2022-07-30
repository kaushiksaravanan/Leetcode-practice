class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        x=set()
        def f(index,flag):
            if index>=len(s):
                l=0
                ss=''
                for i in flag:
                    if i==1:
                        ss+=s[l].lower()
                    if i==0:
                        ss+=s[l].upper()
                    l+=1
                x.add(ss[:])
                return
            flag[index]=1
            f(index+1,flag)
            flag[index]=0
            f(index+1,flag)
        f(0,[-1]*len(s))
        return x
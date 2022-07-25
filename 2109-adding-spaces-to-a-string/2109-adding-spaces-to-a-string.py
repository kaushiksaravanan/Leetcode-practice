class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        x=''
        l=0
        ind=0
        n=len(spaces)
        for i in s:
            print(ind)
            if ind<n and spaces[ind]==l:
                ind+=1
                x+=' '
            x+=i
            l+=1
        return x
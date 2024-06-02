class Solution:
    def minimumChairs(self, s: str) -> int:
        a=0
        c=0
        for i in s:
            print(a,c)
            if i=='E':
                    a=max(a,c)
                    c+=1
                    a=max(a,c)
                    # a+=1
            if i=='L':
                c-=1
        a=max(a,c)
        return a
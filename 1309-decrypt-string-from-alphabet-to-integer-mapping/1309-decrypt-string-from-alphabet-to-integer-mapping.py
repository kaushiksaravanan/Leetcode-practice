class Solution:
    def freqAlphabets(self, s: str) -> str:
        # s=s.replace('#','?#')
        # m=s.split('#')
        # print(m)
        m=[]
        i=0
        while i<len(s)-2:
            print(i)
            if s[i+2]!='#':
                m.append(s[i])
                i+=1
            else:
                m.append(s[i:i+2]+'?')
                i+=3
        print(m)
        if s[-1]!='#' and s[-2]!='#':
            m.append(s[-2:])
        if s[-2]=='#':
            m.append(s[-1])
        print(m)
        ans=''
        apl='abcdefghijklmnopqrstuvwxyz'
        for i in m:
            if len(i)!=0:
                if i[-1]!='?':
                    for lett in i:
                        print(lett)
                        print(int(lett))
                        ans+=apl[int(lett)-1]
                else:
                    ans+=apl[int(i[:-1])-1]
        return ans
                
        
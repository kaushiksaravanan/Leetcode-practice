class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        plus=-1
        dot=-1
        at=-1
        s=set()
        for i in emails:
            try:
                plus=i.index('+')
            except:
                plus=-1
            try:
                dot=i.index('.')
            except:
                dot=-1
            try:
                at=i.index('@')
            except:
                at=-1
            if at!=-1:
                k=i[:at]
                end=i[at:]
                # if plus!=-1 and dot!=-1 and at!=-1:
                if plus!=-1:
                    k=k[:plus]
                if plus<at:
                    k=k[:at].replace('+','')
                if dot<at:
                    k=k[:at].replace('.','')
                k+=end
                k=k.lower()
                s.add(k)
                print(plus,dot,at)
            plus=-1
            dot=-1
            at=-1
        print(s)
        return len(s)
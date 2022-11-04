class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        m=0
        k=[]
        for e in words:
            b=True
            for lett in e:
                if e.count(lett)<=chars.count(lett):
                    b=True
                else:
                    b=False
                if b==False:
                    break
            if b:
                k.append(e)
                m+=len(e)
        print(k)
        return m
        
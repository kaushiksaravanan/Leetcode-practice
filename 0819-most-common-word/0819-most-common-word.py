class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        paragraph=paragraph.replace(',',' ')
        paragraph=paragraph.replace('.',' ')
        paragraph=paragraph.replace('!',' ')
        paragraph=paragraph.replace('?',' ')
        paragraph=paragraph.replace(';',' ')
        paragraph=paragraph.replace("'",' ')
        paragraph=paragraph.replace('"',' ')
        # paragraph=paragraph.replace('?',' ')

        print(paragraph)
        d={}
        for i in paragraph.split():
            i=i.strip()
            if i not in banned:
                if i in d:
                    d[i]+=1
                if i not in d:
                    d[i]=1
        print(d)
        k=sorted(d,key=lambda y:d[y],reverse=True)
        return k[0]
        
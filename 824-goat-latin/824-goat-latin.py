class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        k=""
        curr=1
        for i in sentence.split():
            e=i[0]
            if e=='a' or e=='e' or e=='i' or e=='o' or e=='u' or e=='A' or e=='E' or e=='I' or e=='O' or e=='U':
                k+=i
                k+='ma'
            else:
                k+=i[1:]
                k+=e
                k+='ma'
            for le in range(curr):
                k+='a'
            if len(sentence.split())!=curr:
                k+=' '
            curr+=1
        return k
            
                
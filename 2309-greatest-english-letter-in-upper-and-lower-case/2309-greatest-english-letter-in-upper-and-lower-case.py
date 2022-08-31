class Solution:
    def greatestLetter(self, s: str) -> str:
        d={}
        # print(ord('a')-ord('A'))
        k=[]
        for i in s:
            d[i]=1
        for i in s:
            #i is cap then find small
            if i.isupper():
                # k=i.lower()
                if i.lower() in d:
                    k.append(i)
                    # k.append(i)

            # else:
            #     if chr(ord(i)+32) in d:
            #         k.append(chr(ord(i)+32))
            #         # k.append(i)

        print(k)
        k.sort()
        if len(k)>=1:
            return k[-1]
        print(k)
        return ""
                
                
                
        
                
                
                
        
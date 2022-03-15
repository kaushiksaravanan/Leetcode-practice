class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        prev=bin(first).replace("0b","")
        y=[]
        y.append(first)
        for i in encoded:
            k=bin(i).replace("0b","")
            cur_max=max(len(prev),len(k))
            len_k=cur_max-len(k)
            len_prev=cur_max-len(prev)
            k=k[::-1]+("0"*len_k)
            prev=prev[::-1]+("0"*len_prev)
            prev=prev[::-1]
            k=k[::-1]
            
            print(k,prev)
            l=""
            for i in range(len(prev)):
                if (k[i]=="1" and prev[i]=="0") or (k[i]=="0" and prev[i]=="1"):
                    l+="1"
                else:
                    l+="0"
            # l=l[::-1]
            y.append(int(l,2))
            prev=bin(int(l,2)).replace("0b","")
        # y.append(prev)
        return y
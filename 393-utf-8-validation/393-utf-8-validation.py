class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        k=[]
        for i in data:
            n1=bin(i)[2:][:8]
            temp_n1=len(n1)
            m=(8-temp_n1)*'0'+n1
            k.append(m)
        def check_1(m,ind):
            return m[ind][0]=='0'
        def check_2(m,ind):
            s1=m[ind][:3]=='110'
            if len(m)<=ind+1:
                return False
            s2=m[ind+1][:2]=='10'
            return s1 and s2
        def check_3(m,ind):
            s1=m[ind][:4]=='1110'
            if len(m)<=ind+1 or len(m)<=ind+2:
                return False
            s2=m[ind+1][:2]=='10'
            s3=m[ind+2][:2]=='10'
            return s1 and s2 and s3
        def check_4(m,ind):
            s1=m[ind][:5]=='11110'
            if len(m)<=ind+1 or len(m)<=ind+2 or len(m)<=ind+3:
                return False
            s2=m[ind+1][:2]=='10'
            s3=m[ind+2][:2]=='10'
            s4=m[ind+2][:2]=='10'
            return s1 and s2 and s3 and s4
        i=0
        print(k)
        while i<len(k):
            print(i)
            if check_1(k,i):
                i+=1
                continue
                # print(i)
            else:
                if check_2(k,i):
                    i+=2
                    continue
                else:
                    print(i)
                    if check_3(k,i):
                        i+=3
                        continue
                    else:
                        if check_4(k,i):
                            i+=4
                            continue
                        else:
                            return False
        return True
        
        print(k)
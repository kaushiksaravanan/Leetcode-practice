class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n=len(password)
        if n>=8:
            uc=0
            lc=0
            d=0
            s=0
            pre=password[0]
            for i in password:
                if i.islower():
                    lc+=1
                if i.isupper():
                    uc+=1
                try:
                    y=int(i)
                    d+=1
                except:
                    pass
                if i in "!@#$%^&*()-+":
                    s+=1
            for i in password[1:]:
                if i==pre:
                    print('nd')
                    return False
                pre=i
                
            print(s,uc,lc,d)
            if s>=1 and uc>=1 and lc>=1 and d>=1:
                return True
            return False
        return False
        
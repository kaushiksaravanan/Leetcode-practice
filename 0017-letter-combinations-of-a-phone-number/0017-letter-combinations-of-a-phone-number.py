class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a=[]
        d={"2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]}
        try:
            a.append(d[digits[0]])
            a=a[0]
        except:
            pass
        # a=a[0]
        print(a)
        def recu(digits):
            
            if len(digits)>0:
                k=[]
                for i in a:
                    d={"2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]}
                    for j in d[digits[0]]:
                        print(j,d[digits[0]],digits)
                        print(i,j)
                        k.append(i+j)
                a[:]=[]
                a.append(k)
                a[:]=a[0]


                print(k)
                recu(digits[1:])
        recu(digits[1:])
        try:
            return a
        except:
            return a
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        full=strs[0]
        for i in strs:
            if len(full)==0:
                return ""
            for l in range(len(i)):
                if len(full)<=l:
                    full=full[:l]
                    break

                if full[l]!=i[l]:
                    full=full[:l]
                    print(full,'broken')
                    break
            if len(full)>len(i):
                full=full[:len(i)-len(full)]
                
        return full
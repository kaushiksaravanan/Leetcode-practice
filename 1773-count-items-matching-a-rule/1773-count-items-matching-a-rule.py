class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "name":
            a=ruleValue
            b=2
        if ruleKey == "type":
            a=ruleValue
            b=0
        if ruleKey == "color":
            a=ruleValue
            b=1
        k=0
        for i in items:
            if i[b]==a:
                k+=1
        return k
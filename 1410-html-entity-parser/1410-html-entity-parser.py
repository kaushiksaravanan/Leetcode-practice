class Solution:
    def entityParser(self, text: str) -> str:
        d={'&quot;':'"?*',
           '&apos;':"'?*", 
           '&amp;':'&?*',
           '&gt;':'>?*',
           '&lt;':'<?*',
           '&frasl;':'/?*',
          '?*':''}
        for i in d:
            text=text.replace(i,d[i])
        return text
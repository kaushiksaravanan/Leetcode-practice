class Solution:
def uniqueMorseRepresentations(self, words: List[str]) -> int:
s=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
ap='abcdefghijklmnopqrstuvwxyz'
w=[]
for i in words:
k=''
for j in i:
k+=s[ap.index(j)]
w.append(k)
return len(set(w))
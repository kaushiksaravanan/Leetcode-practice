class Solution:
def minTimeToType(self, word: str) -> int:
alp='abcdefghijklmnopqrstuvwxyz'
# print(len(alp))
c=0
prev='a'
l=0
le=len(word)
for i in word:
new_pos=alp.index(i)
old_pos=alp.index(prev)
prev=i
diff=new_pos-old_pos
print(diff,end='________')
if diff>13:
diff=26%diff
if diff<0 and diff<-13:
diff=26+diff
else:
diff=abs(diff)
# elif diff<0 and diff
print(diff)
diff+=1
c+=diff
# print(new_pos,old_pos)
return c
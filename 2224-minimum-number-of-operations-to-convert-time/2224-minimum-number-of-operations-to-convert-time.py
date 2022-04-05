class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cou_60=0
        diff=int(correct[-2:])-int(current[-2:])+60*(int(correct[:2])-int(current[:2]))
        while diff>0:
            y=diff//60
            diff-=y*60
            cou_60+=y
            y=diff//15
            diff-=y*15
            cou_60+=y
            y=diff//5
            diff-=y*5
            cou_60+=y
            y=diff
            diff-=y
            cou_60+=y
        return cou_60
        
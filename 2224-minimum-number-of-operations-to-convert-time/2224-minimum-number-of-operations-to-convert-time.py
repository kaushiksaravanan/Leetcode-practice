class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_hr=int(current[:2])
        curr_min=int(current[-2:])
        corr_hr=int(correct[:2])
        corr_min=int(correct[-2:])
        cou_60=0
        diff=corr_min-curr_min+60*(corr_hr-curr_hr)
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
        
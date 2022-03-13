class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        k=1
        for i in sentence.split():
            # print(i)
            for j in range(len(i)+1):
                # print(j)
                if i[:j]==searchWord:
                    # print(i[:j])
                    return k
                else:
                    continue
            k+=1
        return -1
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CountS, CountT = {}, {}
        for i in s:
            try:
                if CountS[i]:
                    CountS[i] += 1 
            except KeyError:
                CountS[i] = 1
        for j in t:
            try:
                if CountT[j]:
                    CountT[j] += 1 
            except KeyError:
                CountT[j] = 1   
        return CountS == CountT

        
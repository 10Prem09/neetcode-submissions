class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CountS, CountT = {}, {}
        for i,j in zip(s,t):
            if i in CountS.keys():
                CountS[i] += 1 
            else: 
                CountS[i] = 1
            if j in CountT.keys():
                CountT[j] += 1 
            else: 
                CountT[j] = 1   
        return CountS == CountT

        
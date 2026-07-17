class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CountS, CountT = {}, {}
        for i in s:
            if i in CountS: # O(1) as Checking index in Hashmap
                    CountS[i] += 1 
            else:
                CountS[i] = 1
        for j in t:
            if j in CountT:
                    CountT[j] += 1 
            else:
                CountT[j] = 1   
        return CountS == CountT

    # Here even though we store CountS and CountT, Space complexity is O(1) as
    # it is constant with respect to change in array size. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in mapSet:
                mapSet.remove(s[l])
                l+=1
            mapSet.add(s[r])
            res = max(res,len(mapSet))
        return res
        
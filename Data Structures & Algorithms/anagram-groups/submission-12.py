class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            indexlist = [0]*26
            for c in s:
                indexlist[ord(c) - ord('a')] +=1
            groups[tuple(indexlist)].append(s)
        return list(groups.values())

